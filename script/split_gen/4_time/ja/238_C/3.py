def main():
    n = int(input())
    ans = 0
    for i in range(1, n + 1):
        ans += len(str(i)) * (n // i)
        ans %= 998244353
    print(ans)
