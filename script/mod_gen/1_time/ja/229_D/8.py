def main():
    S = input()
    K = int(input())
    N = len(S)
    #Xの連続個数を記録する配列
    X = []
    #Xの連続個数を記録する
    for i in range(N):
        if i == 0:
            X.append(1)
        else:
            if S[i] == S[i-1]:
                X[-1] += 1
            else:
                X.append(1)
    #Xの連続個数が奇数の時、その数を2で割る
    for i in range(len(X)):
        if X[i] % 2 == 1:
            X[i] //= 2
    #Xの連続個数を累積和にする
    for i in range(1,len(X)):
        X[i] += X[i-1]
    #Xの連続個数が奇数の時、その数を2で割る
    for i in range(len(X)):
        if X[i] % 2 == 1:
            X[i] //= 2
    #Xの連続個数の累積和の最大値を求める
    ans = 0
    for i in range(len(X)):
        if i+2*K+1 < len(X):
            ans = max(ans,X[i+2*K+1]-X[i])
        else:
            ans = max(ans,X[-1]-X[i])
    #Xの連続個数の累積和の最大値がNより大きい時、Nを出力する
    if ans > N:
        print(N)
    else:
        print(ans)

if __name__ == '__main__':
    main()