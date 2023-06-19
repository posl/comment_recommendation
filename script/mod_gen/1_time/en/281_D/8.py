def solve(n,k,d):
    a = list(map(int,input().split()))
    s = set()
    for i in range(n):
        s.add(a[i])
        for j in range(i+1,k+i):
            s.add(a[i]+a[j])
    for i in range(10**9,-1,-1):
        if i*d in s:
            return i*d
    return -1
n,k,d = map(int,input().split())
print(solve(n,k,d))
