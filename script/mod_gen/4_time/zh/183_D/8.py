def main():
    n,w=map(int,input().split())
    #s=[0]*n
    #t=[0]*n
    #p=[0]*n
    #for i in range(n):
    #    s[i],t[i],p[i]=map(int,input().split())
    #s,t,p=map(list,zip(*sorted(zip(s,t,p))))
    #print(s,t,p)
    #for i in range(n):
    #    if i==0:
    #        if p[i]>w:
    #            print("No")
    #            exit(0)
    #        else:
    #            w-=p[i]
    #    else:
    #        if s[i]-t[i-1]>0:
    #            w+=p[i-1]
    #        if p[i]>w:
    #            print("No")
    #            exit(0)
    #        else:
    #            w-=p[i]
    #print("Yes")
    imos=[0]*(200001)
    for i in range(n):
        s,t,p=map(int,input().split())
        imos[s]+=p
        imos[t]-=p
    for i in range(1,200001):
        imos[i]+=imos[i-1]
        if imos[i]>w:
            print("No")
            exit(0)
    print("Yes")

if __name__ == '__main__':
    main()