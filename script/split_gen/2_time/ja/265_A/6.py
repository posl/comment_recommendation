def main():
    x, y, n = map(int, input().split())
    print(n * x if n < 3 else n * x + (n // 3) * (y - x))
