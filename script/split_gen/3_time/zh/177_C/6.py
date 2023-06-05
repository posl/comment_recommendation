def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += a[i] * a[j]
            ans %= mod
    print(ans)
