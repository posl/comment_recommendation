Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    # 读入数据
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    # 从左上角开始，向右下方向走，求和
    # 从右下角开始，向左上方向走，求和
    # 两个和相加，减去中间重复计算的值
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 += int(a[0][i])
        sum1 += int(a[i][0])
        sum2 += int(a[n-1][i])
        sum2 += int(a[i][n-1])
    sum1 -= int(a[0][0])
    sum1 -= int(a[n-1][n-1])
    print(sum1 + sum2)

=======
Suggestion 3

def get_max_num(N, grid):
    max_num = 0
    for i in range(N):
        for j in range(N):
            max_num = max(max_num, grid[i][j])
    return max_num

=======
Suggestion 4

def get_max_num(N, A):
    max = 0
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            if i == 0:
                max = max * 10 + A[i][j]
                continue
            if j == 0:
                max = max * 10 + A[i][j]
                continue
            if i == N - 1:
                max = max * 10 + A[i][j]
                continue
            if j == N - 1:
                max = max * 10 + A[i][j]
                continue
            max = max * 10 + A[i][j]
    return max

=======
Suggestion 5

def solve():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(8):
                ni = i
                nj = j
                for l in range(N):
                    ni += di[k]
                    nj += dj[k]
                    if ni < 0:
                        ni = N - 1
                    elif ni == N:
                        ni = 0
                    if nj < 0:
                        nj = N - 1
                    elif nj == N:
                        nj = 0
                    ans = max(ans, int(A[ni][nj]))
    print(ans)

di = [1, 1, 1, 0, -1, -1, -1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]

=======
Suggestion 6

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input())))
    ans = -1
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i == n - 1 and j == n - 1:
                continue
            num = a[i][j]
            x = 0
            y = 0
            for k in range(n - 1):
                if x == 0 and y == 0:
                    if i + 1 < n:
                        x = i + 1
                        y = j
                    else:
                        x = i
                        y = j + 1
                elif x == n - 1 and y == n - 1:
                    if i > 0:
                        x = i - 1
                        y = j
                    else:
                        x = i
                        y = j - 1
                elif x == 0:
                    if y + 1 < n:
                        x = i
                        y = j + 1
                    else:
                        x = i + 1
                        y = j
                elif x == n - 1:
                    if y > 0:
                        x = i
                        y = j - 1
                    else:
                        x = i - 1
                        y = j
                elif y == 0:
                    if x > 0:
                        x = i - 1
                        y = j
                    else:
                        x = i
                        y = j + 1
                elif y == n - 1:
                    if x + 1 < n:
                        x = i + 1
                        y = j
                    else:
                        x = i
                        y = j - 1
                elif x + 1 < n and y + 1 < n:
                    x = x + 1
                    y = y + 1
                elif x > 0 and y > 0:
                    x = x - 1
                    y = y - 1
                num = num * 10 + a[x][y]
            if ans < num:
                ans = num
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    A = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        A[i] = list(map(int, input()))
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(8):
                ni, nj = i, j
                for l in range(n-1):
                    ni += dx[k]
                    nj += dy[k]
                    if ni == n:
                        ni = 0
                    if nj == n:
                        nj = 0
                    ans = max(ans, A[ni][nj])
    print(ans)

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
main()

=======
Suggestion 8

def readInput():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int,input())))
    return N,A

=======
Suggestion 9

def main():
    n = int(input())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input())))
    ans = 0
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                continue
            ans = max(ans, grid[i-1][j-1]*1000 + grid[i-1][j]*100 + grid[i-1][j+1]*10 + grid[i][j+1])
            ans = max(ans, grid[i-1][j]*1000 + grid[i-1][j+1]*100 + grid[i][j+1]*10 + grid[i+1][j+1])
            ans = max(ans, grid[i-1][j+1]*1000 + grid[i][j+1]*100 + grid[i+1][j+1]*10 + grid[i+1][j])
            ans = max(ans, grid[i][j+1]*1000 + grid[i+1][j+1]*100 + grid[i+1][j]*10 + grid[i+1][j-1])
            ans = max(ans, grid[i+1][j+1]*1000 + grid[i+1][j]*100 + grid[i+1][j-1]*10 + grid[i][j-1])
            ans = max(ans, grid[i+1][j]*1000 + grid[i+1][j-1]*100 + grid[i][j-1]*10 + grid[i-1][j-1])
            ans = max(ans, grid[i+1][j-1]*1000 + grid[i][j-1]*100 + grid[i-1][j-1]*10 + grid[i-1][j])
            ans = max(ans, grid[i][j-1]*1000 + grid[i-1][j-1]*100 + grid[i-1][j]*10 + grid[i-1][j+1])
    print(ans)
