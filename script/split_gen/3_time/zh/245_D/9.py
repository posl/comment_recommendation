def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = [0]*(m+1)
    for i in range(n+1):
        b[0] += a[i]*c[i]
    for j in range(1,m+1):
        for i in range(n+1):
            b[j] += a[i]*c[i+j]
    for i in range(m):
        print(b[i],end=' ')
    print(b[m])
main()
