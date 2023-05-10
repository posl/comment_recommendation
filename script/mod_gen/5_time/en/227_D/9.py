def solve(N, K, A):
    A.sort(reverse=True)
    ans = 0
    if N == K:
        return 1
    for i in range(N):
        if i < K:
            ans += A[i]
    return ans

if __name__ == '__main__':
    solve()