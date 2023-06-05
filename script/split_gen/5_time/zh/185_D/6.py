def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.append(N+1)
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    if M == 1:
        print(N-1)
        return
    B = []
    for i in range(M):
        if A[i+1]-A[i]-1 > 0:
            B.append(A[i+1]-A[i]-1)
    B.sort()
    k = B[0]
    ans = 0
    for i in B:
        ans += (i+k-1)//k
    print(ans)
solve()
