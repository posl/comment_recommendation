def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, K, A)
    #前処理
    #累積和をとる
    S = [0]
    for i in range(N):
        S.append(S[-1]+A[i])
    #print(S)
    #累積和の差をとる
    T = []
    for i in range(N):
        T.append(S[i+1]-K)
    #print(T)
    #Tの要素をソートする
    T.sort()
    #print(T)
    #Tの要素の個数をカウントする
    #同じ要素の個数をカウントする
    #print(T.count(T[0]))
    ans = 0
    for i in range(N):
        ans += T.count(T[i])
    print(ans)

if __name__ == '__main__':
    main()