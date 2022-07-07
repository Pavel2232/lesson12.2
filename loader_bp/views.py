import logging
from json import JSONDecodeError

from flask import Blueprint,render_template,request, send_from_directory
from functions import add_post, save_pic
loader_bp_blueprint = Blueprint('loader_bp_blueprint', __name__, template_folder= 'templates')



@loader_bp_blueprint.route('/post')
def page_post():
    '''Страница с добавление поста'''
    return render_template('post_form.html')

@loader_bp_blueprint.route('/post', methods=['POST'])
def page_post_upload():
    '''Страница с добавлением поста'''
    picture = request.files.get('picture')
    content = request.form['content']
    if not picture or not content:
        return f'Нет картинки или текста'

    if picture.filename.split('.')[-1] not in ['jpeg', 'png']:
        logging.info('Файл не найден')
        return 'Неверный формат'
    try:
        filename = '/' + save_pic(picture)
    except FileNotFoundError:
        return 'Файл не найден'
    except JSONDecodeError:
        return 'Файл не подходит'
    post = add_post({'pic': filename , 'content': content })
    return render_template('post_uploaded.html', post= post)


@loader_bp_blueprint.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)