def solve():
    a,b,k = map(int, input().split())
    if a >= b:
        print(0)
    else:
        print((b - a - 1) // (k - 1) + 1)
