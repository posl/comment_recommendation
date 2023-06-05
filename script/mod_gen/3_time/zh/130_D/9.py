def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    ans = 0
    right = 0
    for left in range(N):
        while right < N+1 and S[right] - S[left] < K:
            right += 1
        ans += N - right + 1
    print(ans)

if __name__ == '__main__':
    solve()