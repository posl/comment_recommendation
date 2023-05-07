def solve():
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 998244353
    ans = 0
    for i in range(1, 1 << N):
        cnt = 0
        sum = 0
        for j in range(N):
            if i >> j & 1:
                cnt += 1
                sum += A[j]
        if sum % cnt == 0:
            ans += 1
    print(ans % MOD)

if __name__ == '__main__':
    solve()