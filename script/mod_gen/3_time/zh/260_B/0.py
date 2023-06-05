def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],a[i],i+1])
    c.sort(reverse=True)
    d = []
    for i in range(x):
        d.append(c[i])
    d.sort(key=lambda x:x[2])
    for i in range(y):
        d.append(c[x+i])
    d.sort(key=lambda x:x[2])
    for i in range(z):
        d.append(c[x+y+i])
    d.sort(key=lambda x:x[2])
    for i in range(len(d)):
        print(d[i][2])

if __name__ == '__main__':
    main()