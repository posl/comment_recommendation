def main():
    n, k = map(int, input().split())
    mod = pow(10, 9) + 7
    ans = 0
    for i in range(k, n + 2):
        ans += (n - i + 1) * (n + i + 1) // 2 - (i - 1) * i // 2 + 1
        ans %= mod
    print(ans)
