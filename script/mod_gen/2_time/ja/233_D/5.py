def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #累積和のリストを作る
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])
    #辞書を作る
    D = {}
    for i in range(N+1):
        if S[i] in D:
            D[S[i]].append(i)
        else:
            D[S[i]] = [i]
    #計算
    ans = 0
    for i in range(N+1):
        if K + S[i] in D:
            ans += len(D[K + S[i]])
    print(ans)

if __name__ == '__main__':
    main()