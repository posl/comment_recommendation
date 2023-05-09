def main():
    n,m=map(int,input().split())
    l=[0]*(n+1)
    r=[0]*(n+1)
    for i in range(m):
        a,b=map(int,input().split())
        l[a]+=1
        r[b]+=1
    for i in range(1,n+1):
        l[i]+=l[i-1]
    for i in range(n-1,0,-1):
        r[i]+=r[i+1]
    ans=0
    for i in range(1,n+1):
        if l[i-1]+r[i+1]==m:
            ans+=1
    print(ans)

if __name__ == '__main__':
    main()