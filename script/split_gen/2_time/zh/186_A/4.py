def main():
    n,m = map(int,input().split())
    if m == 0:
        print(1)
        return
    a = [int(i) for i in input().split()]
    a.sort()
    k = n
    for i in range(m-1):
        k = min(k,a[i+1]-a[i]-1)
    k = min(k,n-a[-1])
    print((n+k-1)//k)
