def problem120_a():
    a, b, c = map(int, input().split())
    if a > b:
        print(0)
    else:
        print(b // a if c > b // a else c)
problem120_a()
