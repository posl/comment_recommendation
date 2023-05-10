def dice(a,b,c):
    if a==b:
        return c
    elif b==c:
        return a
    elif c==a:
        return b
    else:
        return 0
a,b,c = map(int, input().split())
print(dice(a,b,c))
