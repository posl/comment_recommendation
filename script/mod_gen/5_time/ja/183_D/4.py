def main():
    N, W = map(int, input().split())
    S = []
    T = []
    P = []
    for i in range(N):
        s, t, p = map(int, input().split())
        S.append(s)
        T.append(t)
        P.append(p)
    #print(N, W)
    #print(S)
    #print(T)
    #print(P)
    #配列の最大値を取得する
    max_t = max(T)
    #print(max_t)
    #最大値分の配列を作成する
    use = [0] * (max_t + 1)
    #print(use)
    #各人の利用量を配列に格納する
    for i in range(N):
        use[S[i]] += P[i]
        use[T[i]] -= P[i]
    #print(use)
    #累積和を取得する
    for i in range(max_t):
        use[i + 1] += use[i]
    #print(use)
    #最大値がWを超えていたらNo
    for i in range(max_t):
        if use[i] > W:
            print('No')
            return
    print('Yes')
    return

if __name__ == '__main__':
    main()