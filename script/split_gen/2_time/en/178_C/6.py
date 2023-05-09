def main():
    n = int(input())
    mod = 10**9 + 7
    ans = 0
    for i in range(1, n + 1):
        ans += i * pow(10, i, mod) * pow(9, n - i, mod)
        ans %= mod
    print(ans)
