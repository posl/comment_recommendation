def solve():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    minv = 100
    for i in range(H):
        for j in range(W):
            minv = min(minv, A[i][j])
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - minv
    print(ans)

if __name__ == '__main__':
    solve()