def solve(n,k,m,a):
    sum = 0
    for i in range(n-1):
        sum += a[i]
    x = n*m - sum
    if x>k:
        return -1
    elif x<0:
        return 0
    else:
        return x
n,k,m = map(int,input().split())
a = list(map(int,input().split()))
print(solve(n,k,m,a))
