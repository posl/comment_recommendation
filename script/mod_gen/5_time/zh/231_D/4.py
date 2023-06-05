def main():
    n,m=map(int,input().split())
    a=[0]*n
    b=[0]*n
    for i in range(m):
        a[i],b[i]=map(int,input().split())
    for i in range(m):
        a[i]-=1
        b[i]-=1
    a.sort()
    b.sort()
    for i in range(m-1):
        if b[i]==a[i+1]:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()