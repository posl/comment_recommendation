def solve(n,m,a):
    if n < sum(a):
        return -1
    return n - sum(a)
n,m = map(int,input().split())
a = list(map(int,input().split()))
print(solve(n,m,a))
