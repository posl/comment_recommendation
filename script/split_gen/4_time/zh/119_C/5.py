def dfs(a,b,c,mp):
    if a==b==c:
        return mp
    if a==0 or b==0 or c==0:
        return float('inf')
    return min(dfs(a-1,b+1,c+1,mp+1),dfs(a-1,b,c,c+10),dfs(a,b-1,c+1,mp+1),dfs(a,b-1,c,c+10),dfs(a,b,c-1,mp+1),dfs(a,b,c-1,c+10))
n,a,b,c=map(int,input().split())
l=[]
for i in range(n):
    l.append(int(input()))
l.sort(reverse=True)
print(dfs(a,b,c,0))
