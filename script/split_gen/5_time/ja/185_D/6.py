def main():
    n,m = map(int,input().split())
    if m == 0:
        print(1)
        return
    if n == m:
        print(0)
        return
    a = list(map(int,input().split()))
    a.sort()
    if m == 1:
        print(n-1)
        return
    d = []
    for i in range(1,m):
        d.append(a[i]-a[i-1]-1)
    d.sort()
    k = a[0]-1
    k += n-a[m-1]
    for i in range(m-1):
        k += d[i]
    print(k)
