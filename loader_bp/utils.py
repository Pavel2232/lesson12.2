import json
from functions import read_file


def add_post(post):
    """Запись поста в файл"""
    posts: list[dict] = read_file()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f)
    return post


def save_pic(pic):
    """Сохранение картинки в файл"""
    filename = pic.filename
    path = f'./uploads/images/{filename}'
    pic.save(path)
    return path
