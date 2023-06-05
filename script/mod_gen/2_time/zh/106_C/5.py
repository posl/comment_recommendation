def get_next(s):
    next_s = ''
    for i in s:
        next_s += i*i
    return next_s

if __name__ == '__main__':
    get_next()