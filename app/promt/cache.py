# app/prompt/cache.py
import redis, hashlib, json

r = redis.Redis()

def cached_prompt(prompt):
    key = hashlib.md5(prompt.encode()).hexdigest()
    if r.exists(key):
        return r.get(key).decode()

    return None
