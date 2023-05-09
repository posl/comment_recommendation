def main():
    n,a,b,c=map(int,input().split())
    l=[int(input()) for _ in range(n)]
    ans=10**9
    for i in range(4**n):
        mp=0
        s=[0,0,0,0]
        for j in range(n):
            s[i%(4**(j+1))//(4**j)]+=l[j]
            if i%(4**(j+1))//(4**j)==1:
                mp+=a
            elif i%(4**(j+1))//(4**j)==2:
                mp+=b
            elif i%(4**(j+1))//(4**j)==3:
                mp+=c
        if s[0]==0 or s[1]==0 or s[2]==0:
            continue
        mp+=abs(a-s[0])+abs(b-s[1])+abs(c-s[2])
        ans=min(ans,mp)
    print(ans)

if __name__ == '__main__':
    main()