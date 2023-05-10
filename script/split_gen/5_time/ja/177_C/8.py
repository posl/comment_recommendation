def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(n):
        ans += a[i] * sum(a[i+1:])
    print(ans % mod)
