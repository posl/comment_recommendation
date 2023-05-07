def solve():
    """
    頂点iと頂点jの距離がkになるような整数の組(i,j)(1≦i<j≦N)の数を求める
    """
    N, X, Y = map(int, input().split())
    ans = [0] * N
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            d = min(j - i, abs(X - i) + 1 + abs(Y - j))
            ans[d] += 1
    for k in range(1, N):
        print(ans[k])

if __name__ == '__main__':
    solve()