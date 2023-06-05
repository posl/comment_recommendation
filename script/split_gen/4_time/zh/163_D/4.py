def main():
    n, k = map(int, input().split())
    mod = 10**9 + 7
    if n == k:
        print(1)
    else:
        print(((n - k + 1) * (n + k) // 2) % mod)
