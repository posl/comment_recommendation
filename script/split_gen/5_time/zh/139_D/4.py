def solve(n):
    if n==1:
        return 0
    if n%2==0:
        return n*(n-1)//2
    else:
        return n*(n-1)//2+(n-1)//2
