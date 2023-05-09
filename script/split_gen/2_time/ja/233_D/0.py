def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    S = [0]*(N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    D = dict()
    for i in range(N+1):
        if S[i] in D:
            D[S[i]] += 1
        else:
            D[S[i]] = 1
    ans = 0
    for i in range(N+1):
        if S[i] + K in D:
            ans += D[S[i]+K]
    print(ans)
