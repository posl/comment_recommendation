def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, N+1):
        if i == M:
            ans = max(ans, sum(A[:i]))
        elif i > M:
            ans = max(ans, sum(A[:i]) + sum(A[-(i-M):]))
    print(ans)

if __name__ == '__main__':
    solve()