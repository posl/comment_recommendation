def main():
    #入力
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    
    #累積和
    s = [0]
    for i in range(N):
        s.append(s[i]+A[i])
    
    #辞書
    d = {}
    for i in range(N+1):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    
    #答え
    ans = 0
    for i in range(N+1):
        if s[i] - K in d:
            ans += d[s[i]-K]
    
    print(ans)

if __name__ == '__main__':
    main()