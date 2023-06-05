def main():
    x,y = map(int,input().split())
    mod = 10**9+7
    if (x+y)%3 != 0:
        print(0)
        return
    n = (x+y)//3
    m = x-n
    if m<0 or n<0:
        print(0)
        return
    if m>n:
        m,n = n,m
    if m==0:
        print(1)
        return
    ans = 1
    for i in range(1,m+1):
        ans = ans*(n-m+i)%mod
        ans = ans*pow(i,mod-2,mod)%mod
    print(ans)

if __name__ == '__main__':
    main()