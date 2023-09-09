from functools import wraps

def memo(f):
    cache = {}
    @wraps(f)
    def _cache(*args):
        if args in cache.keys():
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result
    return _cache

@memo
def drops(n, k):
    if n == 1 or k == 1 or k == 0:
        return k
    result = 0
    for i in range(1, k):
        t1 = drops(n - 1, i)
        t2 = drops(n, k - i)
        result = max(result, min(t1, t2) + 1)
    return result
