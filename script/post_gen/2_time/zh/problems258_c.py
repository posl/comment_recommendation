Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int,input())))
    # print(a)
    # print(a[0][0])
    # print(a[1][1])
    # print(a[2][2])
    # print(a[3][3])
    # print(a[0][3])
    # print(a[1][2])
    # print(a[2][1])
    # print(a[3][0])
    maxnum = 0
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                maxnum = max(maxnum,a[i][j]+a[i+1][j]+a[i][j+1]+a[i+1][j+1])
            elif i == 0 and j == n-1:
                maxnum = max(maxnum,a[i][j]+a[i+1][j]+a[i][j-1]+a[i+1][j-1])
            elif i == n-1 and j == 0:
                maxnum = max(maxnum,a[i][j]+a[i-1][j]+a[i][j+1]+a[i-1][j+1])
            elif i == n-1 and j == n-1:
                maxnum = max(maxnum,a[i][j]+a[i-1][j]+a[i][j-1]+a[i-1][j-1])
            elif i == 0:
                maxnum = max(maxnum,a[i][j]+a[i][j-1]+a[i][j+1]+a[i+1][j]+a[i+1][j-1]+a[i+1][j+1])
            elif i == n-1:
                maxnum = max(maxnum,a[i][j]+a[i][j-1]+a[i][j+1]+a[i-1][j]+a[i-1][j-1]+a[i-1][j+1])
            elif j == 0:
                maxnum = max(maxnum,a[i][j]+a[i-1][j]+a[i+1][j]+a[i][j+1]+a[i-1][j+1]+a[i+1][j+1])
            elif j == n-1:

=======
Suggestion 3

def get_max_value(n, grid):
    # 1. 从第一行的第一个开始，每次向右移动一格，到最后一行的第一个
    # 2. 从第一行的第一个开始，每次向右移动一格，到最后一行的倒数第二个
    # 3. 从第一行的第一个开始，每次向右移动一格，到最后一行的倒数第三个
    # 4. 从第一行的第一个开始，每次向右移动一格，到最后一行的倒数第四个
    # 5. 从第一行的第一个开始，每次向右移动一格，到最后一行的倒数第五个
    # 6. 从第一行的第一个开始，每次向右移动一格，到最后一行的倒数第六个
    # 7. 从第一行的第一个开始，每次向右移动一格，到最后一行的倒数第七个
    # 8. 从第一行的第一个开始，每次向右移动一格，到最后一行的倒数第八个
    # 9. 从第一行的第一个开始，每次向右移动一格，到最后一行的倒数第九个
    # 10. 从第一行的第一个开始，每次向右移动一格，到最后一行的倒数第十个
    # 11. 从第一行的第二个开始，每次向右移动一格，到最后一行的第二个
    # 12. 从第一行的第三个开始，每次向右移动一格，到最后一行的第三个
    # 13. 从第一行的第四个开始，每次向右移动一格，到最后一行的第四个
    # 14. 从第一行的第五个开始，每次

=======
Suggestion 4

def main():
    N = int(input())
    grid = []
    for i in range(N):
        grid.append(list(map(int, input())))
    ans = 0
    for i in range(N):
        for j in range(N):
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue
                    tmp = grid[i][j]
                    ni, nj = i, j
                    for k in range(N - 1):
                        ni += di
                        nj += dj
                        if ni == -1:
                            ni = N - 1
                        elif ni == N:
                            ni = 0
                        if nj == -1:
                            nj = N - 1
                        elif nj == N:
                            nj = 0
                        tmp *= 10
                        tmp += grid[ni][nj]
                    ans = max(ans, tmp)
    print(ans)

=======
Suggestion 5

def dfs(i, j, k, n, a, used):
    if k == n:
        return 0
    res = 0
    used[i][j] = True
    res = max(res, dfs(i - 1, j, k + 1, n, a, used) * 10 + a[i][j])
    res = max(res, dfs(i + 1, j, k + 1, n, a, used) * 10 + a[i][j])
    res = max(res, dfs(i, j - 1, k + 1, n, a, used) * 10 + a[i][j])
    res = max(res, dfs(i, j + 1, k + 1, n, a, used) * 10 + a[i][j])
    used[i][j] = False
    return res

n = int(input())
a = [list(map(int, input())) for _ in range(n)]
used = [[False] * n for _ in range(n)]
res = 0
for i in range(n):
    for j in range(n):
        res = max(res, dfs(i, j, 0, n, a, used))
print(res)

=======
Suggestion 6

def readInput():
    N = int(input())
    A = []
    for i in range(N):
        A.append(input())
    return N, A

=======
Suggestion 7

def get_max_number(grid):
    N = len(grid)
    max_number = 0
    for i in range(N):
        for j in range(N):
            # 从（i,j）开始，向右走
            number = 0
            for k in range(N):
                number *= 10
                number += grid[i][(j + k) % N]
            max_number = max(max_number, number)
            # 从（i,j）开始，向下走
            number = 0
            for k in range(N):
                number *= 10
                number += grid[(i + k) % N][j]
            max_number = max(max_number, number)
            # 从（i,j）开始，向右下走
            number = 0
            for k in range(N):
                number *= 10
                number += grid[(i + k) % N][(j + k) % N]
            max_number = max(max_number, number)
            # 从（i,j）开始，向左下走
            number = 0
            for k in range(N):
                number *= 10
                number += grid[(i + k) % N][(j - k) % N]
            max_number = max(max_number, number)
    return max_number

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input())))
    ans = -1
    for i in range(n):
        for j in range(n):
            for k in range(8):
                x = i
                y = j
                s = str(a[x][y])
                for l in range(n - 1):
                    x += dx[k]
                    y += dy[k]
                    s += str(a[x][y])
                ans = max(ans, int(s))
    print(ans)

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
