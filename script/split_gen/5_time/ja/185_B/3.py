def solve():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    now = N
    for i in range(M):
        now -= A[i] - B[i-1] if i > 0 else A[i]
        if now <= 0:
            print("No")
            return
        now += B[i] - A[i]
    now -= T - B[-1]
    if now <= 0:
        print("No")
        return
    print("Yes")
