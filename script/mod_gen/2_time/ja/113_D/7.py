def memoize(f):
    cache = {}
    def _f(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return _f
@memoize

if __name__ == '__main__':
    memoize()