def main():
    N,K = map(int,input().split())
    Ps = list(map(int,input().split()))
    #累積和
    S = [0]
    for i in range(N):
        S.append(S[i]+Ps[i])
    #print(S)
    #期待値
    E = []
    for i in range(N-K+1):
        E.append((S[i+K]-S[i]+K)/2)
    print(max(E))

if __name__ == '__main__':
    main()