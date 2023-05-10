def main():
    N,M=map(int,input().split())
    k=[0]*M
    s=[0]*M
    p=[0]*M
    for i in range(M):
        k[i],*s[i]=map(int,input().split())
    p=list(map(int,input().split()))
    ans=0
    for i in range(2**N):
        for j in range(M):
            cnt=0
            for l in range(k[j]):
                if (i>>(s[j][l]-1))&1:
                    cnt+=1
            if cnt%2==p[j]:
                if j==M-1:
                    ans+=1
            else:
                break
    print(ans)
