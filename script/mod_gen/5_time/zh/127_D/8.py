def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = []
    c = []
    for i in range(m):
        x,y = map(int,input().split())
        b.append(x)
        c.append(y)
    sum = 0
    for i in range(n):
        sum += a[i]
    for i in range(m):
        sum += (c[i]-a[b[i]-1])
    print(sum)
main()
