def solve():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    ans = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            dist = min(j - i, abs(X - i) + 1 + abs(Y - j))
            ans[dist] += 1
    for i in range(1, N):
        print(ans[i])

if __name__ == '__main__':
    solve()