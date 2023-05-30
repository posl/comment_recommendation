def floor(a,b):
    return int(a/b)
A,B,N = map(int,input().split())
x = min(B-1,N)
print(floor(A*x/B)-A*floor(x/B))
