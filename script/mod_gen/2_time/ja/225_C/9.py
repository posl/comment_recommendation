def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    # N行M列のBの最小値を取得
    minB = min([min(b) for b in B])
    # Bの最小値のインデックスを取得
    for i in range(N):
        for j in range(M):
            if B[i][j] == minB:
                minI = i
                minJ = j
    # Bの最小値のインデックスを基準にAの最小値を探索
    for i in range(minI, N):
        for j in range(minJ, M):
            if B[i - minI][j - minJ] != minB + (i - minI) * 7 + (j - minJ):
                print("No")
                return
    print("Yes")

if __name__ == '__main__':
    main()