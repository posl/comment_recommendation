def dfs(x,y):
    #print(x,y)
    if (x,y) in black:
        black.remove((x,y))
        dfs(x-1,y-1)
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y)
        dfs(x+1,y+1)
N=int(input())
black=[]
for i in range(N):
    x,y=map(int,input().split())
    black.append((x,y))
ans=0
while black:
    ans+=1
    dfs(black[0][0],black[0][1])
print(ans)
