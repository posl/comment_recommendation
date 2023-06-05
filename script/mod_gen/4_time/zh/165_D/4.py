def solve(A,B,N):
    x = min(B-1,N)
    return (A*x)//B - A*(x//B)
A,B,N = map(int,input().split())
print(solve(A,B,N))
