def solve():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    ans = K
    for i in range(N):
        if i == 0:
            ans = min(ans, K - A[N - 1] + A[1] - A[0])
        elif i == N - 1:
            ans = min(ans, K - A[N - 2] + A[N - 1] - A[0])
        else:
            ans = min(ans, K - A[i - 1] + A[i + 1] - A[i])
    print(ans)

if __name__ == '__main__':
    solve()