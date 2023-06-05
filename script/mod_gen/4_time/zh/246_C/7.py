def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] >= X:
            ans += A[i] - X
        else:
            ans += A[i]
    print(ans)

if __name__ == '__main__':
    solve()