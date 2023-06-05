def median(a, b, c):
    if a < b:
        if b < c:
            return b
        else:
            if a < c:
                return c
            else:
                return a
    else:
        if a < c:
            return a
        else:
            if b < c:
                return c
            else:
                return b
a, b, c = map(int, input().split())
print('是' if b == median(a, b, c) else '否')
