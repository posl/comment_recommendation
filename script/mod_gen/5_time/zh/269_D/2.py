def dfs(x,y):
    if not(0<=x<=2000 and 0<=y<=2000):
        return
    if not (x,y) in d:
        return
    if d[(x,y)]:
        return
    d[(x,y)]=True
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)
n=int(input())
d={}
for i in range(n):
    x,y=map(int,input().split())
    d[(x,y)]=False
cnt=0
for i in range(n):
    if not d[(x,y)]:
        cnt+=1
        dfs(x,y)
print(cnt)

if __name__ == '__main__':
    dfs()