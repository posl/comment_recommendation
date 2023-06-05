def main():
    n,c = map(int,input().split())
    a,b,cc = [0]*n,[0]*n,[0]*n
    for i in range(n):
        a[i],b[i],cc[i] = map(int,input().split())
        b[i] += 1
    d = [0]*(10**9+2)
    for i in range(n):
        d[a[i]] += cc[i]
        d[b[i]] -= cc[i]
    for i in range(10**9+1):
        d[i+1] += d[i]
    print(min(c,min(d[1:])))
main()
