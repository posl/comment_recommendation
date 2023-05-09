def solve():
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    B = A.copy()
    for i in range(P-1,Q):
        B[R-1+i-Q] = A[i]
    for i in range(R-1,S):
        B[P-1+i-R+Q] = A[i]
    print(*B)

if __name__ == '__main__':
    solve()