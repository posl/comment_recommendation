def solve(N,K,A):
    l = 0
    r = 0
    sum = 0
    cnt = 0
    while (r < N):
        sum += A[r]
        r += 1
        while (sum >= K):
            cnt += N - r + 1
            sum -= A[l]
            l += 1
    return cnt

if __name__ == '__main__':
    solve()