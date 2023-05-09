def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],a[i],b[i],i+1])
    c.sort(key=lambda x:(-x[0],-x[1],-x[2],x[3]))
    for i in range(x+y+z):
        print(c[i][3])

if __name__ == '__main__':
    main()