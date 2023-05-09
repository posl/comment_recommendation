def main():
    n = int(input())
    a = list(map(int,input().split()))
    ans = 0
    mod = 10**9+7
    for i in range(60):
        zero = 0
        one = 0
        for j in range(n):
            if a[j]>>i & 1:
                one += 1
            else:
                zero += 1
        ans += (zero*one)%mod * pow(2,i,mod)%mod
        ans %= mod
    print(ans)
