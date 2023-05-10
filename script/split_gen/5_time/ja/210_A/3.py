def main():
    n, a, x, y = map(int, input().split())
    print(min(n, a) * x + max(n - a, 0) * y)
