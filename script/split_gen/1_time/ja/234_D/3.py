def main():
    #入力
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    #累積和
    cumsum = [0]*(N+1)
    for i in range(N):
        cumsum[i+1] = cumsum[i] + P[i]
    #出力
    for i in range(K,N+1):
        print(cumsum[i]-cumsum[i-K])
