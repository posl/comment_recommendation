def solve():
    n,m,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.append(0)
    b.append(0)
    for i in range(1,n+1):
        a[i] += a[i-1]
    for i in range(1,m+1):
        b[i] += b[i-1]
    ans = 0
    j = m
    for i in range(n+1):
        if a[i] > k:
            break
        while a[i] + b[j] > k:
            j -= 1
        ans = max(ans,i+j)
    print(ans)
