def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = []
    for i in range(m):
        if i == 0:
            b.append(a[i]-1)
        else:
            b.append(a[i]-a[i-1]-1)
    if m > 0:
        b.append(n-a[m-1])
    b.sort()
    ans = 0
    for i in range(m+1):
        if b[i] > 0:
            ans += b[i]
    print(ans)
