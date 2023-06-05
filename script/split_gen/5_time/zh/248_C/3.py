def f(n, m, k):
    if n==1:
        return m
    if k==0:
        return 1
    if k<0:
        return 0
    if k>m*n:
        return 0
    return f(n-1, m, k)+f(n, m, k-1)
n, m, k = map(int, input().split())
print(f(n, m, k))
