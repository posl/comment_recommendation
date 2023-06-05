def main():
    n,k=map(int,input().split())
    s=input()
    t=[0]*(n+1)
    for i in range(n):
        t[i+1]=t[i]+int(s[i])
    ans=0
    for i in range(n):
        l=max(0,i-k)
        r=min(n,i+k)
        ans=max(ans,t[r]-t[l])
    print(ans)

if __name__ == '__main__':
    main()