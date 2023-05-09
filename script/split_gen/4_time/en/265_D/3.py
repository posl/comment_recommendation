def problems265_d():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                ans = max(ans, P*A[i]+Q*A[j]+R*A[k])
    print(ans)
