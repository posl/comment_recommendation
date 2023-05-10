def main():
    n=int(input())
    A=[list(map(int, input().split())) for _ in range(n)]
    ans=0
    for i in range(1<<n):
        t=0
        for j in range(n):
            for k in range(j+1,n):
                if (i>>j&1)==(i>>k&1)==1:
                    t+=A[j][k]
        ans=max(ans,t)
    print(ans)
