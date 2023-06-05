def solve():
    N,X = map(int,input().split())
    A = []
    B = []
    for _ in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    # print(A)
    # print(B)
    # print(X)
    ans = 10**18
    for i in range(N):
        t = A[i]
        ans = min(ans,t*X)
        t = A[i] + B[i]
        ans = min(ans,t*X + A[i])
        t = A[i] + B[i] + B[i]
        ans = min(ans,t*X + A[i] + B[i])
        t = A[i] + B[i] + B[i] + B[i]
        ans = min(ans,t*X + A[i] + B[i] + B[i])
    print(ans)
