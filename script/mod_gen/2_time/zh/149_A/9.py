def solve(N, A):
    # N = int(input())
    # A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] == i + 1:
            ans += 1
    if ans == N:
        return 0
    elif ans == N - 1:
        return 1
    else:
        return N - ans

if __name__ == '__main__':
    solve()