def main():
    #入力
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    #初期化
    now = 0
    time = T
    #処理
    for i in range(N-1):
        time -= A[i] #移動時間を減らす
        for j in range(M):
            if X[j] == i+1 and time + Y[j] > T:
                time = T #ボーナス部屋の処理
            elif X[j] == i+1:
                time += Y[j] #ボーナス部屋の処理
        if time <= 0:
            now = i+1 #移動できない部屋を記録
            break
    #出力
    if now == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()