def main():
    n,m = map(int,input().split())
    #print(n,m)
    #print(10**9+7)
    #print(10**5)
    #print(10**9)
    #print(10**9+7)
    #print(10**5)
    #print(10**9)
    #print(10**9+7)
    #print(10**5)
    #print(10**9)
    #print(10**9+7)
    #print(10**5)
    #print(10**9)
    #print(10**9+7)
    #print(10**5)
    #print(10**9)
    #print(10**9+7)
    #print(10**5)
    #print(10**9)
    #print(10**9+7)
    #print(10**5)
    #print(10**9)
    #print(10**9+7)
    #print(10**5)
    #print(10**9)
    #print(10**9+7)
    #print(10**5)
    #print(10**9)
    #print(10**9+7)
    #print(10**5)
    #print(10**9)
    #print(10**9+7)
    ans = 1
    for i in range(2,int(m**0.5)+1):
        if m%i == 0:
            cnt = 0
            while m%i == 0:
                cnt += 1
                m //= i
            ans *= cnt+n-1
            ans %= 10**9+7
    if m != 1:
        ans *= 1+n-1
        ans %= 10**9+7
    print(ans)

if __name__ == '__main__':
    main()