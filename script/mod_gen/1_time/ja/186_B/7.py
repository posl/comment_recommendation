def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    #print(A)
    # 全てのマスの合計値の平均を求める
    sum = 0
    for i in range(H):
        for j in range(W):
            sum += A[i][j]
    ave = sum / (H * W)
    #print(ave)
    # 全てのマスの合計値の平均を超えないようにブロックを取り除く
    ans = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] > ave:
                ans += A[i][j] - ave
    print(int(ans))

if __name__ == '__main__':
    main()