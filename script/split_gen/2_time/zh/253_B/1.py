def findNext(x,y):
    if x+1<H:
        if S[x+1][y]=='-':
            S[x+1][y]=S[x][y]+1
            findNext(x+1,y)
    if x-1>=0:
        if S[x-1][y]=='-':
            S[x-1][y]=S[x][y]+1
            findNext(x-1,y)
    if y+1<W:
        if S[x][y+1]=='-':
            S[x][y+1]=S[x][y]+1
            findNext(x,y+1)
    if y-1>=0:
        if S[x][y-1]=='-':
            S[x][y-1]=S[x][y]+1
            findNext(x,y-1)
H,W=map(int,input().split())
S=[list(input()) for i in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j]=='o':
            S[i][j]=0
            findNext(i,j)
print(max(max(S)))
