def main():
    n,x=map(int,input().split())
    a=[0]*n
    b=[0]*n
    for i in range(n):
        a[i],b[i]=map(int,input().split())
    ans=0
    for i in range(n):
        ans+=a[i]*b[i]
    if ans<=x:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()