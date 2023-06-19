def solve():
    N, M, T = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    charge = N
    pre = 0
    for i in range(M):
        charge -= A[i] - pre
        if charge <= 0:
            return False
        charge = min(N, charge + B[i] - A[i])
        pre = B[i]
    charge -= T - pre
    if charge <= 0:
        return False
    return True
print("Yes" if solve() else "No")
