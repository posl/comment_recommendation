def main():
    x,y=map(int,input().split())
    mod=10**9+7
    if (x+y)%3!=0:
        print(0)
        return
    n=(x+y)//3
    m=min(x,y)-n
    if m<0:
        print(0)
        return
    ans=1
    for i in range(m):
        ans=ans*(n-i)%mod
    for i in range(1,m+1):
        ans=ans*pow(i,mod-2,mod)%mod
    print(ans)
