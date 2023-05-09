def main():
    x, y, n = map(int, input().split())
    print(min(x * n, y * (n // 3) + x * (n % 3)))
