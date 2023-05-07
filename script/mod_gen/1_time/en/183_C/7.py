def main():
    n,k=map(int,input().split())
    a=[list(map(int,input().split())) for i in range(n)]
    ans=0
    for i in range(1,n):
        for j in range(i+1,n):
            a[i][j]+=a[j][i]
    for i in range(1,n):
        for j in range(i+1,n):
            if a[i][j]>k:
                continue
            for l in range(j+1,n):
                if a[i][j]+a[j][l]<=k:
                    ans+=1
    print(ans*6)

if __name__ == '__main__':
    main()