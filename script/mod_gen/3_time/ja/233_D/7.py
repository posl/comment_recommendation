def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    #Aの累積和を求める
    s = [0]*(N+1)
    for i in range(N):
        s[i+1] = s[i] + A[i]
    #累積和の値をキーに、その値が出現するインデックスを値とする辞書を作成
    d = {}
    for i in range(N+1):
        if s[i] in d:
            d[s[i]].append(i)
        else:
            d[s[i]] = [i]
    #累積和の値にKを足した値が辞書のキーに存在するかを確認
    #存在する場合、そのキーに対応するインデックスの組み合わせをカウントする
    ans = 0
    for i in range(N+1):
        if s[i]+K in d:
            ans += len(d[s[i]+K])
    print(ans)

if __name__ == '__main__':
    main()