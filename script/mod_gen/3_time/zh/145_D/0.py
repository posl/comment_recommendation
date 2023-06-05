def main():
    x,y=map(int,input().split())
    if (x+y)%3!=0:
        print(0)
        return
    if x>y:
        x,y=y,x
    if x*2<y:
        print(0)
        return
    n=(x+y)//3
    x-=n
    y-=2*n
    ans=1
    m=10**9+7
    for i in range(1,n+1):
        ans=ans*(n-i+1)%m
        ans=ans*pow(i,m-2,m)%m
    print(ans)

if __name__ == '__main__':
    main()