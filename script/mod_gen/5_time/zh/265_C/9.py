def move(i,j):
    if G[i-1][j-1] == "U" and i!=1:
        return i-1,j
    elif G[i-1][j-1] == "D" and i!=H:
        return i+1,j
    elif G[i-1][j-1] == "L" and j!=1:
        return i,j-1
    elif G[i-1][j-1] == "R" and j!=W:
        return i,j+1
    else:
        return -1,-1
H,W = map(int,input().split())
G = [list(input()) for i in range(H)]
i,j = 1,1
seen = [[0 for i in range(W)] for j in range(H)]
seen[0][0] = 1
while True:
    i,j = move(i,j)
    if i==-1 and j==-1:
        print(-1)
        break
    elif seen[i-1][j-1] == 1:
        print(i,j)
        break
    else:
        seen[i-1][j-1] = 1

if __name__ == '__main__':
    move()