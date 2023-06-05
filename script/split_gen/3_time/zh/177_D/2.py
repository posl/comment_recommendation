def main():
    n,m = map(int,input().split())
    a = [0]*n
    b = [0]*n
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    a = a[:m]
    b = b[:m]
    a = a[:m]
    b = b[:m]
    print(a,b)
    ans = 0
    f = [0]*n
    for i in range(m):
        f[a[i]] += 1
        f[b[i]] += 1
    for i in range(n):
        ans = max(ans,f[i])
    print(ans)
