def solve():
    a, b, c = map(int, input().split())
    if b >= a * c:
        return c
    else:
        return b // a
print(solve())
