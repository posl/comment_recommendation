def main():
    D,G=map(int,input().split())
    p=[]
    c=[]
    for i in range(D):
        p1,c1=map(int,input().split())
        p.append(p1)
        c.append(c1)
    ans=10**9
    for i in range(2**D):
        s=0
        cnt=0
        rest_max=-1
        for j in range(D):
            if (i>>j)&1:
                s+=100*(j+1)*p[j]+c[j]
                cnt+=p[j]
            else:
                rest_max=j
        if s<G:
            s1=100*(rest_max+1)
            need=(G-s+s1-1)//s1
            if need>=p[rest_max]:
                continue
            cnt+=need
        ans=min(ans,cnt)
    print(ans)

if __name__ == '__main__':
    main()