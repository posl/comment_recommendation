def solve():
    # write your code here
    N = int(input())
    A = list(map(int, input().split()))
    MOD = 10**9 + 7
    ans = 0
    for i in range(60):
        count = 0
        for j in range(N):
            if A[j] & (1 << i):
                count += 1
        ans += (count * (N - count) * (1 << i)) % MOD
    print(ans % MOD)

if __name__ == '__main__':
    solve()