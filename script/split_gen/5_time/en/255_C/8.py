def solve(x,a,d,n):
    if a <= x <= a + (n-1)*d:
        return 0
    elif a > x:
        return -1
    else:
        return 1 + solve(x+d,a,d,n)
x,a,d,n = map(int,input().split())
print(solve(x,a,d,n))
