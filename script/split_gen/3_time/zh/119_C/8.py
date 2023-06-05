def dfs(a,b,c,mp):
    if a == 0 and b == 0 and c == 0:
        return mp
    if a < 0 or b < 0 or c < 0:
        return 1000000
    res = 1000000
    res = min(res,dfs(a-l[0],b,c,mp+1))
    res = min(res,dfs(a,b-l[0],c,mp+1))
    res = min(res,dfs(a,b,c-l[0],mp+1))
    res = min(res,dfs(a-l[0],b-l[0],c,mp+1))
    res = min(res,dfs(a-l[0],b,c-l[0],mp+1))
    res = min(res,dfs(a,b-l[0],c-l[0],mp+1))
    res = min(res,dfs(a-l[0],b-l[0],c-l[0],mp+1))
    return res
n,a,b,c = map(int,input().split())
l = []
for i in range(n):
    l.append(int(input()))
print(dfs(a,b,c,0))
