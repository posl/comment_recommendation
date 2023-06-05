def solve():
    N,M,T = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    now = 0
    for i in range(M):
        if i == 0:
            now += A[i] - 0
        else:
            now += A[i] - B[i-1]
        if now >= N:
            now = N
        now -= B[i] - A[i]
        if now <= 0:
            print('No')
            return
    if now - T + B[-1] >= 0:
        print('Yes')
    else:
        print('No')
solve()
