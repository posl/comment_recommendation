def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([i+1,a[i],b[i],a[i]+b[i]])
    c.sort(key=lambda x:(-x[1],-x[2],-x[3],x[0]))
    for i in range(x+y+z):
        print(c[i][0])

if __name__ == '__main__':
    main()