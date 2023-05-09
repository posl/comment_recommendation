def main():
    x, y, n = map(int, input().split())
    print(int((n + 2) * x - (n - 2) * y))
