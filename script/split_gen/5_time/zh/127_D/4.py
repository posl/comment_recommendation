def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = [0]*m
    c = [0]*m
    for i in range(m):
        b[i],c[i] = map(int,input().split())
    a.sort()
    c.sort()
    ans = 0
    for i in range(n):
        ans += a[i]
    j = n-1
    for i in range(m):
        if a[j] < c[i]:
            ans += c[i]-a[j]
            j -= 1
        else:
            break
    print(ans)
