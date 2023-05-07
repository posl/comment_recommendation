def main():
    #入力
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*M
    Y = [0]*M
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    #初期化
    t = T
    #処理
    for i in range(N-1):
        t -= A[i]
        if t <= 0:
            print("No")
            return
        for j in range(M):
            if X[j] == i+1:
                t += Y[j]
                break
    #出力
    if t > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()