def solve(A,B,C):
    if A==0 and B==0 and C==0:
        return 0
    else:
        return (A*solve(A-1,B,C)+B*solve(A+1,B-1,C)+C*solve(A,B+1,C-1))/(A+B+C)+1
A,B,C=map(int,input().split())
print(solve(A,B,C))
