import json

POSTS_PATH = "posts.json"


def read_file() -> list[dict]:
    '''словарь постов'''
    with open(POSTS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def search_post(key) -> list[dict]:
    '''Поиск поста по ключу'''
    posts = read_file()
    result = []
    for keys in posts:
        if key.lower() in keys["content"].lower():
            result.append(keys)
    return result


def add_post(post):
    '''Запись поста в файл'''
    posts: list[dict] = read_file()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f)
    return post


def save_pic(pic):
    '''Сохранение картинки в файл'''
    filename = pic.filename
    path = f'./uploads/images/{filename}'
    pic.save(path)
    return path
