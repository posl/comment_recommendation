def main():
    n, k, a = map(int, input().split())
    print((k + a - 1) % n + 1)
