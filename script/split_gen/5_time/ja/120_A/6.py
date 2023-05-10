def calc():
    a, b, c = map(int, input().split())
    if a * c > b:
        return b // a
    else:
        return c
print(calc())
