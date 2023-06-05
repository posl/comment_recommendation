def main():
    n,a,b,c = map(int, input().split())
    l = [int(input()) for _ in range(n)]
    ans = 10**9
    for i in range(4**n):
        mp = 0
        abc = [0,0,0]
        for j in range(n):
            if (i>>2*j)&1:
                mp+=10
                continue
            if abc[0]!=0:
                mp+=abs(abc[0]-l[j])
            abc[0]=l[j]
        for j in range(n):
            if (i>>2*j)&1==0:
                mp+=10
                continue
            if abc[1]!=0:
                mp+=abs(abc[1]-l[j])
            abc[1]=l[j]
        for j in range(n):
            if (i>>2*j)&1==0:
                mp+=10
                continue
            if abc[2]!=0:
                mp+=abs(abc[2]-l[j])
            abc[2]=l[j]
        if abc[0]*abc[1]*abc[2]==0:continue
        mp+=abs(abc[0]-a)+abs(abc[1]-b)+abs(abc[2]-c)
        ans=min(ans,mp)
    print(ans)
