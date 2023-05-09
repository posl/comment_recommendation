def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9+7
    ans = 0
    for i in range(60):
        x = 0
        for j in range(n):
            if a[j]>>i & 1:
                x += 1
        ans += x*(n-x)*pow(2,i,mod)
        ans %= mod
    print(ans)
