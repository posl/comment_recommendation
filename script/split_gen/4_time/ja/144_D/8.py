def solve():
    a, b, x = map(int, input().split())
    if a*a*b/2 <= x:
        return 90 - (a*a*b-x)*2/a/a
    else:
        return 90 - x*2/a/b/b
print(solve())
