def max_num(a, b):
    if a+b > a-b and a+b > a*b:
        return a+b
    elif a-b > a+b and a-b > a*b:
        return a-b
    else:
        return a*b
