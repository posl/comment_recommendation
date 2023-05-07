def main():
    #入力
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #初期化
    ans = 0
    #処理
    #Aの要素の総和を求める
    for i in range(N):
        ans += A[i]
    #x=1~N,y=1~Nの場合の総和を求める
    for i in range(1,N+1):
        for j in range(1,N+1):
            #Aの要素をL,Rで置き換える
            for k in range(i):
                A[k] = L
            for k in range(j):
                A[N-1-k] = R
            #Aの要素の総和を求める
            tmp = 0
            for k in range(N):
                tmp += A[k]
            #最小値を求める
            if tmp < ans:
                ans = tmp
    #出力
    print(ans)

if __name__ == '__main__':
    main()