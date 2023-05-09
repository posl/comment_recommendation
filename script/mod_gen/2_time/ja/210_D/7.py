def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    # 駅の建設費用の最小値を求める
    B = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == j == 0:
                B[i][j] = A[i][j]
            elif i == 0:
                B[i][j] = min(B[i][j - 1], A[i][j])
            elif j == 0:
                B[i][j] = min(B[i - 1][j], A[i][j])
            else:
                B[i][j] = min(B[i - 1][j], B[i][j - 1], A[i][j])
    # 最小値を使って線路の建設費用を求める
    ans = float("inf")
    for i in range(H):
        for j in range(W):
            ans = min(ans, A[i][j] + B[i][j] + C * (i + j))
    print(ans)

if __name__ == '__main__':
    main()