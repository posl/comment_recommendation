def resolve():
    N,K = map(int,input().split())
    h = []
    for i in range(N):
        h.append(int(input()))
    h.sort()
    ans = 10**9
    for i in range(N-K+1):
        tmp = h[i+K-1]-h[i]
        if tmp < ans:
            ans = tmp
    print(ans)
