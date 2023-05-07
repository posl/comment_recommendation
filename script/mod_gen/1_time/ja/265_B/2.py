def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * M
    Y = [0] * M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    #print(N, M, T)
    #print(A)
    #print(X)
    #print(Y)
    #初期値
    t = T
    n = 1
    #print(t, n)
    #部屋1から部屋Nへ移動
    for i in range(N - 1):
        #print("i=", i)
        #print(t, n)
        #持ち時間を消費して部屋i+1へ移動
        t -= A[i]
        #print(t, n)
        #持ち時間が0以下になるような移動は行わない
        if t <= 0:
            print("No")
            return
        #部屋i+1に到達したらボーナス部屋かチェック
        if n == X[i]:
            t += Y[i]
        #print(t, n)
        #部屋i+1に到達したら部屋i+2に移動
        n += 1
        #print(t, n)
        #print()
    #最後の部屋へ移動した後に持ち時間が0以下になるような移動は行わない
    t -= A[N - 1]
    #print(t, n)
    if t <= 0:
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()