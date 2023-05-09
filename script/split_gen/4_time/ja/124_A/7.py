def solve():
    a, b = map(int, input().split())
    if a == b:
        return a + b
    else:
        return max(a + a - 1, b + b - 1, a + b)
print(solve())
