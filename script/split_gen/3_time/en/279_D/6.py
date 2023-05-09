def solve():
    a, b = map(int, input().split())
    if b >= a:
        return 1 + (a / 2)
    else:
        return 1 + b + (a / (2 * b))
