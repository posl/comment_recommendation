def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    mod = 1000000007
    for i in range(n):
        ans += a[i] * (sum(a[i+1:]) % mod)
    print(ans % mod)
