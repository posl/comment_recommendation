def median(a,b,c):
    if a > b:
        a,b = b,a
    if b > c:
        b,c = c,b
    if a > b:
        a,b = b,a
    return b
a,b,c = map(int, input().split())
print("Yes" if median(a,b,c) == b else "No")
