def solve():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_cnt = 100
    for i in range(H):
        for j in range(W):
            if A[i][j] < min_cnt:
                min_cnt = A[i][j]
    ans = 0
    for i in range(H):
        for j in range(W):
            ans += A[i][j] - min_cnt
    print(ans)

if __name__ == '__main__':
    solve()