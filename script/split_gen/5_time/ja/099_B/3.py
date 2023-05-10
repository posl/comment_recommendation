def solve():
    a, b = map(int, input().split())
    print(b - a - 1 - sum(range(1, b - a)))
