def dfs(a,b,c,mp):
    if a==0 and b==0 and c==0:
        return mp
    if a<0 or b<0 or c<0:
        return 1000000
    if (a,b,c) in memo:
        return memo[(a,b,c)]
    ret = 1000000
    for i in range(N):
        ret = min(ret,dfs(a-l[i],b,c,mp+10),dfs(a,b-l[i],c,mp+10),dfs(a,b,c-l[i],mp+10),dfs(a-l[i],b-l[i],c,mp+10),dfs(a-l[i],b,c-l[i],mp+10),dfs(a,b-l[i],c-l[i],mp+10),dfs(a-l[i],b-l[i],c-l[i],mp+10))
    memo[(a,b,c)] = ret
    return ret
N,A,B,C = map(int,input().split())
l = []
for i in range(N):
    l.append(int(input()))
memo = {}
print(dfs(A,B,C,0))
