def solve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j]
    print(ans - H * W)

if __name__ == '__main__':
    solve()