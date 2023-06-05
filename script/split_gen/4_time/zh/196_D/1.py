def f(m,n):
    if m==0:
        return 1
    if m<0 or n==0:
        return 0
    return f(m,n-1)+f(m-n,n)
H,W,A,B=map(int,input().split())
print(f(H*W-A*2-B,B))
