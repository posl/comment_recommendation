Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                print(0, end='')
            else:
                print(1, end='')
        print('')

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    grid = [[-1 for i in range(N)] for j in range(N)]
    grid[0][0] = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == -1:
                continue
            for k in range(N):
                for l in range(N):
                    if grid[k][l] == -1:
                        if (i-k)**2 + (j-l)**2 == M:
                            grid[k][l] = grid[i][j] + 1
    for i in range(N):
        print(' '.join(map(str, grid[i])))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    if n == 1:
        print(0)
        return
    if m == 1:
        for i in range(n):
            print(i)
        return
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                print(0, end=' ')
                continue
            if i == 1 and j == 0:
                print(1, end=' ')
                continue
            if i == 0 and j == 1:
                print(1, end=' ')
                continue
            if i == 1 and j == 1:
                print(2, end=' ')
                continue
            if i == 0 or j == 0 or i == 1 or j == 1:
                print(2, end=' ')
                continue
            print(3, end=' ')
        print()

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    if m == 1:
        for i in range(n):
            for j in range(n):
                print(i+j)
            print()
        return
    elif m == 2:
        for i in range(n):
            for j in range(n):
                print(1 if (i+j)%2 else 0)
            print()
        return
    elif m == 3:
        for i in range(n):
            for j in range(n):
                print(i if (i+j)%3 == 0 else i+j)
            print()
        return
    elif m == 4:
        for i in range(n):
            for j in range(n):
                print((i//2+j//2)*2 if (i+j)%2 == 0 else (i+j)//2*2+1)
            print()
        return
    elif m == 5:
        for i in range(n):
            for j in range(n):
                print(i+j if (i+j)%5 == 0 else i+j+1)
            print()
        return
    else:
        for i in range(n):
            for j in range(n):
                print(i+j if (i+j)%7 == 0 else i+j+1)
            print()
        return

=======
Suggestion 5

def getDistance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    if n==1:
        print(0)
        return
    if m==1:
        for i in range(n):
            print(i+1)
        return
    #d = [i*i for i in range(1,1000)]
    d = [i*i for i in range(1,1000)]
    d.sort()
    #print(d)
    ans = [[-1 for j in range(n)] for i in range(n)]
    ans[0][0] = 0
    ans[0][1] = 1
    ans[1][0] = 1
    ans[1][1] = 2
    for i in range(2,n):
        ans[0][i] = 2
        ans[i][0] = 2
        ans[1][i] = 3
        ans[i][1] = 3
        ans[i][i] = 4
    for i in range(2,n):
        for j in range(2,i):
            ans[i][j] = 3
            ans[j][i] = 3
    for i in range(2,n):
        for j in range(i+1,n):
            ans[i][j] = 4
            ans[j][i] = 4
    #print(ans)
    for i in range(2,n):
        for j in range(2,i):
            if ans[i][j]==-1:
                if ans[i-1][j]==-1 or ans[i][j-1]==-1:
                    ans[i][j] = 5
                    ans[j][i] = 5
                else:
                    ans[i][j] = ans[i-1][j]+1
                    ans[j][i] = ans[i-1][j]+1
    for i in range(2,n):
        for j in range(i+1,n):
            if ans[i][j]==-1:
                if ans[i-1][j]==-1 or ans[i][j-1]==-1:
                    ans[i][j] = 5
                    ans[j][i] = 5
                else:
                    ans[i][j] = ans[i-1][j]+1
                    ans[j][i] = ans[i-

=======
Suggestion 7

def main():
    N,M = map(int, input().rstrip().split())
    grid = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            grid[i][j] = (i-j)**2+(i+j)**2
    for i in range(N):
        for j in range(N):
            grid[i][j] = int(grid[i][j]**0.5)
    for i in range(N):
        for j in range(N):
            if grid[i][j]**2 == (i-j)**2+(i+j)**2:
                grid[i][j] = -1
    for i in range(N):
        print(' '.join(map(str, grid[i])))

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    m = m**0.5
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    dp = [[-1 for i in range(n)] for j in range(n)]
    dp[0][0] = 0
    queue = [(0,0)]
    while len(queue) > 0:
        x, y = queue.pop(0)
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and dp[nx][ny] == -1 and abs(grid[x][y] - grid[nx][ny]) <= m:
                dp[nx][ny] = dp[x][y] + 1
                queue.append((nx, ny))
    for row in dp:
        print(' '.join(map(str, row)))

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    M = M**0.5
    M = int(M)
    if M*M == M:
        M = M
    else:
        M = M+1
    if M*M < 2:
        M = 2
    if M*M > 10**6:
        M = 10**6
    ans = []
    for i in range(N):
        ans.append([])
        for j in range(N):
            ans[i].append(-1)
    ans[0][0] = 0
    for i in range(N):
        for j in range(N):
            if ans[i][j] == -1:
                continue
            for k in range(-M,M+1):
                for l in range(-M,M+1):
                    if i+k < 0 or i+k >= N or j+l < 0 or j+l >= N:
                        continue
                    if (i+k)**2+(j+l)**2 <= M*M:
                        ans[i+k][j+l] = ans[i][j]+1
    for i in range(N):
        for j in range(N):
            print(ans[i][j],end = " ")
        print()

=======
Suggestion 10

def main():
    N, M = map(
