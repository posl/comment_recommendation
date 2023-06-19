def main():
    n,k=map(int,input().split())
    ans=0
    for a in range(1,n+1):
        if a%k==0:
            ans+=n**3
        else:
            for b in range(1,n+1):
                if (a+b)%k==0:
                    ans+=n**2
                else:
                    for c in range(1,n+1):
                        if (a+b+c)%k==0:
                            ans+=n
    print(ans)
main()
