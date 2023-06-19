def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    X = [int(input()) for _ in range(Q)]
    D = [0] * (N + 1)
    for i in range(N):
        D[i + 1] = D[i] + A[i]
    #print(D)
    for x in X:
        ans = 0
        for i in range(N):
            ans += min(D[i + 1] - D[i],x - D[i])
        print(ans)
main()
