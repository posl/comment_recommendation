def compare_pow(a,b,c):
    if pow(a,c) > pow(b,c):
        return '>'
    elif pow(a,c) < pow(b,c):
        return '<'
    else:
        return '='
