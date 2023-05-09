def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    sum = 0
    l = 0
    for r in range(N):
        sum += A[r]
        while sum >= K:
            ans += N - r
            sum -= A[l]
            l += 1
    print(ans)
