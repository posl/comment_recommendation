def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    r = 0
    tmp = 0
    for l in range(N):
        while r < N and tmp < K:
            tmp += A[r]
            r += 1
        if tmp >= K:
            ans += N - r + 1
        tmp -= A[l]
    print(ans)
