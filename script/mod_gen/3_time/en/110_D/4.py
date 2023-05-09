def main():
    n,m=map(int,input().split())
    ans=1
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            cnt=0
            while m%i==0:
                m//=i
                cnt+=1
            ans*=comb(n+cnt-1,cnt)
            ans%=mod
    if m!=1:
        ans*=n
        ans%=mod
    print(ans)

if __name__ == '__main__':
    main()