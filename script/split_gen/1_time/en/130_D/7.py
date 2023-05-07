def solve():
    N, K = [int(x) for x in input().split(" ")]
    A = [int(x) for x in input().split(" ")]
    cnt = 0
    r = 0
    s = 0
    for l in range(N):
        while r < N and s < K:
            s += A[r]
            r += 1
        if s >= K:
            cnt += N - r + 1
        s -= A[l]
    return cnt
print(solve())
