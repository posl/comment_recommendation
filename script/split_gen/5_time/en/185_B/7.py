def solve():
    n,m,t = map(int,input().split())
    A = []
    B = []
    for _ in range(m):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    charge = n
    prev = 0
    for i in range(m):
        charge -= A[i] - prev
        if charge <= 0:
            return False
        charge += B[i] - A[i]
        if charge > n:
            charge = n
        prev = B[i]
    charge -= t - prev
    if charge <= 0:
        return False
    return True
