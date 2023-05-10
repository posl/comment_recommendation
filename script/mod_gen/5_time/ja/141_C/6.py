def main():
    # データ入力
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    # 各参加者のポイント
    points = [K - Q] * N
    # 正解者のポイントを増やす
    for a in A:
        points[a-1] += 1
    # 各参加者のポイントが 0 以下なら敗退
    for point in points:
        if point <= 0:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()