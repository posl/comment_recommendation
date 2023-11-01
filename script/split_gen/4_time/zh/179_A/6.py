def pluralize(s):
    if s[-1] == 's':
        s += 'es'
    else:
        s += 's'
    return s
