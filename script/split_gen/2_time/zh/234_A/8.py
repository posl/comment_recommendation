def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    r = 0
    s = 0
    for l in range(N):
        while r < N and s + A[r] < K:
            s += A[r]
            r += 1
        ans += r - l
        if r == l:
            r += 1
        else:
            s -= A[l]
    print(ans)
