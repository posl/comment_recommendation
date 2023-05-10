def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    if m == 0:
        print(1)
        exit()
    if n == m:
        print(0)
        exit()
    b = []
    for i in range(m):
        if i == 0:
            b.append(a[i]-1)
        else:
            b.append(a[i]-a[i-1]-1)
    b.append(n-a[m-1])
    b.sort()
    k = b[0]
    ans = 0
    for i in range(m+1):
        if b[i] % k == 0:
            ans += b[i] // k
        else:
            ans += b[i] // k + 1
    print(ans)
