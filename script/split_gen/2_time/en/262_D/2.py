def main():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, 1 << N):
        cnt = 0
        s = 0
        for j in range(N):
            if i >> j & 1:
                cnt += 1
                s += A[j]
        if s % cnt == 0:
            ans += 1
    ans = ans * pow(2, MOD - 2, MOD)
    ans %= MOD
    print(ans)
