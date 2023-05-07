def solve():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > X:
            ans += A[i] - X
    print(max(0, ans - K))

if __name__ == '__main__':
    solve()