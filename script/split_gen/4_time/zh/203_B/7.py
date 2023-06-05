def main():
    n, k = map(int, input().split())
    print((100 * n + 10 * k + 3) * n * k // 2)
