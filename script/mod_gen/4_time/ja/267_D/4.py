def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n-m+1):
        for j in range(m):
            ans+=a[i+j]*(j+1)
    print(ans)

if __name__ == '__main__':
    main()