import json

POSTS_PATH = "posts.json"


def read_file() -> list[dict]:
    """словарь постов"""
    with open(POSTS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
