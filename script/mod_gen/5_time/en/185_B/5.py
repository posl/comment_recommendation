def solve():
    N,M,T = map(int,input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    charge = N
    prev = 0
    for i in range(M):
        charge -= A[i] - prev
        if charge <= 0:
            return False
        charge += B[i] - A[i]
        charge = min(charge,N)
        prev = B[i]
    charge -= T - prev
    if charge <= 0:
        return False
    return True
print("Yes" if solve() else "No")

if __name__ == '__main__':
    solve()