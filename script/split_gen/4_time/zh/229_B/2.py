def easy_or_hard(a,b):
    a = str(a)
    b = str(b)
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    elif len(a) < len(b):
        a = '0' * (len(b) - len(a)) + a
    for i in range(len(a)):
        if int(a[i]) + int(b[i]) > 9:
            return 'Hard'
    return 'Easy'
