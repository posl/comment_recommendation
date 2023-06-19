Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    for i in range(N):
        for j in range(N):
            print(min(abs(i - k) + abs(j - l) for k in range(N) for l in range(N) if (k - i) * (k - i) + (l - j) * (l - j) == M), end=" ")
        print()

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    ans = [[-1 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                ans[i][j] = 0
            elif i == 0:
                ans[i][j] = ans[i][j-1]+1
            elif j == 0:
                ans[i][j] = ans[i-1][j]+1
            else:
                ans[i][j] = min(ans[i-1][j],ans[i][j-1])+1
    for i in range(n):
        for j in range(n):
            if ans[i][j] == -1:
                print(ans[i][j],end=" ")
            else:
                print(ans[i][j]*2,end=" ")
        print()

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    for i in range(n):
        for j in range(n):
            if i==j:
                print(0,end=' ')
            else:
                print(1,end=' ')
        print()

=======
Suggestion 5

def bfs(sx, sy):
    dist = [[-1] * N for _ in range(N)]
    dist[sx][sy] = 0
    que = []
    que.append((sx, sy))
    while que:
        x, y = que.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and dist[nx][ny]==-1:
                dist[nx][ny] = dist[x][y] + 1
                que.append((nx, ny))
    return dist

N, M = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dist = bfs(0, 0)
for i in range(N):
    for j in range(N):
        if dist[i][j] == -1 or dist[i][j] > M:
            print(-1, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                print(0, end=' ')
            elif i == 0:
                print(1, end=' ')
            elif j == 0:
                print(1, end=' ')
            else:
                print(2, end=' ')
        print()

=======
Suggestion 7

def get_nearest_square_number(n):
    for i in range(1, n+1):
        if i**2 > n:
            return i-1

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    m = m**0.5
    m = int(m)
    #print(m)
    for i in range(n):
        for j in range(n):
            if i==0 and j==0:
                print(0,end=' ')
            elif i==0:
                print(j,end=' ')
            elif j==0:
                print(i,end=' ')
            else:
                print(m,end=' ')
        print()
