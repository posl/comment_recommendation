def solve():
    N, D = map(int, input().split())
    L = [0] * N
    R = [0] * N
    for i in range(N):
        L[i], R[i] = map(int, input().split())
    # print(L, R)
    L.sort()
    R.sort()
    # print(L, R)
    ans = 0
    for i in range(N):
        ans += 1
        if L[i] > R[i]:
            ans += 1
    print(ans)
