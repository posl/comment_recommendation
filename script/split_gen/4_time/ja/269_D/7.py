def search(x,y):
    global N
    global X
    global Y
    global visited
    visited[x][y] = True
    for i in range(N):
        if X[i] == x and Y[i] == y:
            break
    if i == N-1:
        return
    if x-1 >= 0 and y-1 >= 0 and visited[x-1][y-1] == False:
        search(x-1,y-1)
    if x-1 >= 0 and visited[x-1][y] == False:
        search(x-1,y)
    if y-1 >= 0 and visited[x][y-1] == False:
        search(x,y-1)
    if y+1 >= 0 and visited[x][y+1] == False:
        search(x,y+1)
    if x+1 >= 0 and visited[x+1][y] == False:
        search(x+1,y)
    if x+1 >= 0 and y+1 >= 0 and visited[x+1][y+1] == False:
        search(x+1,y+1)
N = int(input())
X = []
Y = []
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
visited = [[False for i in range(2001)] for j in range(2001)]
ans = 0
for i in range(N):
    if visited[X[i]+1000][Y[i]+1000] == False:
        search(X[i]+1000,Y[i]+1000)
        ans += 1
print(ans)
