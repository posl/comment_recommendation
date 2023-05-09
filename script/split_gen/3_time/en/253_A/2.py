def median(a,b,c):
    if a > b:
        if b > c:
            return b
        elif a > c:
            return c
        else:
            return a
    else:
        if a > c:
            return a
        elif b > c:
            return c
        else:
            return b
a,b,c = map(int, input().split())
print("Yes" if median(a,b,c) == b else "No")
