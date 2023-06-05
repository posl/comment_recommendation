def main():
    x, y, n = map(int, input().split())
    print(((n + 2) // 3) * x if x * 3 <= y * 2 else (n // 2) * y + (n % 2) * x)
