def main():
    N, M = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(N)]
    # Bの左上の値を取り出す
    a = B[0][0]
    # Aの左上の値を取り出す
    # a = (a-1) * 7 + 1
    # a = a - 1 * 7 - 1
    # a = a - 7 - 1
    # a = a - 8
    a = a - 8
    # Bの値をAの値に変換
    for i in range(N):
        for j in range(M):
            B[i][j] = B[i][j] - a
    # Bの値がAの値かどうかを判定
    for i in range(N):
        for j in range(M):
            if B[i][j] < 1 or B[i][j] > 1000000000:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()