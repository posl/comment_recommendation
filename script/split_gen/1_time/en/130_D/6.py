def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K)
    #print(A)
    ans = 0
    r = 0
    s = 0
    for l in range(N):
        while r < N and s < K:
            s += A[r]
            r += 1
        if s < K:
            break
        ans += N - r + 1
        s -= A[l]
    print(ans)
