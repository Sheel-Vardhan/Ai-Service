# ✅ In-memory cache fallback
# Used because local Redis server is not running properly on Windows

cache_store = {}


def get_cache(key):
    return cache_store.get(key)


def set_cache(key, value):
    cache_store[key] = value