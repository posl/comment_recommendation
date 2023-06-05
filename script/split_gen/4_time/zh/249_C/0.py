def f(a):
    if len(a)==1:
        return 1
    else:
        return len(a)+f(a[1:])
