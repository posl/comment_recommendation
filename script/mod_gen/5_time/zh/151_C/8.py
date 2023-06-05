def main():
    n,m=map(int,input().split())
    p=[0]*n
    s=[0]*n
    for i in range(m):
        tmp=list(input().split())
        p[int(tmp[0])-1]+=1
        if tmp[1]=='AC':
            s[int(tmp[0])-1]=1
    ans=0
    for i in range(n):
        if s[i]==1:
            ans+=1
    s=[0]*n
    for i in range(m):
        tmp=list(input().split())
        if s[int(tmp[0])-1]==0:
            if tmp[1]=='WA':
                s[int(tmp[0])-1]=1
            elif tmp[1]=='AC':
                s[int(tmp[0])-1]=2
    wa=0
    for i in range(n):
        if s[i]==2:
            wa+=p[i]
    print(ans,wa)

if __name__ == '__main__':
    main()