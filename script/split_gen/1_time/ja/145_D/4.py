def main():
    x,y = map(int,input().split())
    if (x+y)%3 != 0:
        print(0)
        exit()
    n = (x+y)//3
    m = min(x,y)-n
    if m < 0:
        print(0)
        exit()
    mod = 10**9+7
    #print(n,m)
    ans = 1
    for i in range(n-m+1,n+1):
        ans *= i
        ans %= mod
    for i in range(1,m+1):
        ans *= pow(i,mod-2,mod)
        ans %= mod
    print(ans)
