def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 998244353
    ans = [0] * 10
    for i in range(10):
        ans[i] = pow(2, n-1, mod) - 1
    for i in range(n):
        ans[a[i]] -= pow(2, n-1-i, mod)
    for i in range(10):
        ans[i] %= mod
    for i in range(10):
        print(ans[i])
