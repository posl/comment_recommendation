def dfs(x,y):
    if x<0 or x>1000 or y<0 or y>1000 or (x,y) in used or (x,y) not in black:
        return
    used.add((x,y))
    for i in range(-1,2):
        for j in range(-1,2):
            if i!=j:
                dfs(x+i,y+j)
n=int(input())
black=set()
for i in range(n):
    x,y=map(int,input().split())
    black.add((x,y))
used=set()
ans=0
for x,y in black:
    if (x,y) not in used:
        ans+=1
        dfs(x,y)
print(ans)

if __name__ == '__main__':
    dfs()