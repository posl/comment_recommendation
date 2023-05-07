def get_next(s):
    next_s = []
    for c in s:
        if c == '1':
            next_s.append('1')
        else:
            next_s.append(c * int(c))
    return ''.join(next_s)
