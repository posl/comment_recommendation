def solve():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    MOD = 10**9+7
    ans = 1
    for i in range(N):
        ans = ans * max(C[i]-i, 0) % MOD
    print(ans)

if __name__ == '__main__':
    solve()