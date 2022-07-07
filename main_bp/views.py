import logging

from flask import Blueprint,render_template,request
from functions import read_file,search_post
main_bp_blueprint = Blueprint('main_bp_blueprint', __name__, template_folder= 'templates')

@main_bp_blueprint.route('/')
def homepage():
    return render_template('index.html')

@main_bp_blueprint.route('/search')
def searchpage():
    '''поисковая строка и страница постов'''
    s = request.args.get('s','')
    logging.info('выполняю поиск')
    try:
        post = search_post(s)
    except FileNotFoundError:
        return 'Файл не найден'
    return render_template('post_list.html',key = s, posts = post)
