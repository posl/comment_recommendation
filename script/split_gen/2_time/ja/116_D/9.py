def main():
    N,K=map(int,input().split())
    sushi=[list(map(int,input().split())) for _ in range(N)]
    sushi.sort(key=lambda x:x[1],reverse=True)#おいしさで降順ソート
    sushi_kind=[0]*(N+1)
    sushi_kind[0]=1
    ans=0
    sum_=0
    kind=0
    for i in range(K):
        sum_+=sushi[i][1]
        kind+=sushi_kind[sushi[i][0]]
        sushi_kind[sushi[i][0]]+=1
    ans=sum_+kind**2
    for i in range(K,N):
        if sushi_kind[sushi[i][0]]==0:
            kind+=1
        sushi_kind[sushi[i][0]]+=1
        sum_+=sushi[i][1]
        sum_-=sushi[i-K][1]
        sushi_kind[sushi[i-K][0]]-=1
        if sushi_kind[sushi[i-K][0]]==0:
            kind-=1
        ans=max(ans,sum_+kind**2)
    print(ans)
