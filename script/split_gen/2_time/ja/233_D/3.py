def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    #累積和
    S = [0]
    for i in range(N):
        S.append(S[i]+A[i])
    #累積和の差がKになる組み合わせを探す
    for i in range(N):
        for j in range(i+1, N+1):
            if S[j]-S[i] == K:
                ans += 1
    print(ans)
