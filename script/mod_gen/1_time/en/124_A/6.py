def solve():
    a, b = map(int, input().split())
    if a == b:
        return 2 * a
    else:
        return 2 * max(a, b) - 1
print(solve())
