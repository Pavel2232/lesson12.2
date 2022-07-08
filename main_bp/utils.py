from functions import read_file


def search_post(key) -> list[dict]:
    """Поиск поста по ключу"""
    posts = read_file()
    result = []
    for keys in posts:
        if key.lower() in keys["content"].lower():
            result.append(keys)
    return result
