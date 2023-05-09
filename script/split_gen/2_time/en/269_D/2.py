def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    # (x, y) -> (x + y, x - y)
    # (x, y) -> (x + y, x - y + 2 * y)
    # (x, y) -> (x + y, x - y + 4 * y)
    # (x, y) -> (x + y, x - y + 6 * y)
    # (x, y) -> (x + y, x - y + 8 * y)
    # (x, y) -> (x + y, x - y + 10 * y)
    # ...
    # (x, y) -> (x + y, x - y + 2 * n * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 1) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 2) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 3) * y)
    # ...
    # (x, y) -> (x + y, x - y + 2 * (n + 1000) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 1001) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 1002) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 1003) * y)
    # ...
    # (x, y) -> (x + y, x - y + 2 * (n + 1000) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 1001) * y)
    # (x, y) -> (x + y, x - y + 2 * (n + 100
