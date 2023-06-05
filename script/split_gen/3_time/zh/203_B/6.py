def main():
    n, k = map(int, input().split())
    print(100 * (n + 1) * n * k // 2)
