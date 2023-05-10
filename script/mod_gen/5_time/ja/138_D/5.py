def main():
    n,q = map(int,input().split())
    a = [0 for i in range(n+1)]
    for i in range(n-1):
        x,y = map(int,input().split())
        a[x] += 1
        a[y] += 1
    b = [0 for i in range(n+1)]
    for i in range(q):
        x,y = map(int,input().split())
        b[x] += y
    for i in range(1,n+1):
        print(a[i]+b[i],end=" ")
    print()

if __name__ == '__main__':
    main()