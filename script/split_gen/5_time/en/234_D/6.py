def problems234_d():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    L = [0] * N
    for i in range(N):
        L[P[i] - 1] = i
    ans = []
    for i in range(K - 1, N):
        ans.append(L[i])
    ans.sort()
    for i in range(len(ans)):
        print(ans[i] + 1)
problems234_d()
