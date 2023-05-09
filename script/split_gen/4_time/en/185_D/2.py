def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if m == 0:
        print(1)
        return
    if n == m:
        print(0)
        return
    d = []
    for i in range(m-1):
        d.append(a[i+1]-a[i]-1)
    d.sort()
    k = a[0]-1
    if k > 0:
        d.append(k)
    k = n-a[-1]
    if k > 0:
        d.append(k)
    k = d[0]
    ans = 0
    for i in range(len(d)):
        ans += (d[i]+k-1)//k
    print(ans)
