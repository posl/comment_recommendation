Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    #输入数据
    h, w, c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    #print(a)
    #计算
    min_co

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def problem210_d():
    pass

=======
Suggestion 4

def get_input():
    input_list = []
    while True:
        input_data = input()
        if input_data == "":
            break
        input_list.append(input_data)
    return input_list

=======
Suggestion 5

def main():
    h,w,c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    ans = 10**18
    for i in range(h):
        for j in range(w):
            for k in range(i,h):
                for l in range(j, w):
                    if i == k and j == l:
                        continue
                    ans = min(ans, a[i][j] + a[k][l] + c * (abs(i-k) + abs(j-l)))
    print(ans)

=======
Suggestion 6

def main():
    #输入
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    #处理
    ans = 10**18
    for _ in range(2):
        dp = [[10**18]*W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j]+C)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1]+C)
                ans = min(ans, dp[i][j]+A[i][j])
        A = [a[::-1] for a in A[::-1]]
    print(ans)

=======
Suggestion 7

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10 ** 18
    for _ in range(2):
        dp = [[10 ** 18] * w for _ in range(h)]
        for i in range(h):
            for j in range(w):
                for di, dj in ((-1, 0), (0, -1)):
                    if i + di >= 0 and j + dj >= 0:
                        dp[i][j] = min(dp[i][j], dp[i + di][j + dj])
                dp[i][j] = min(dp[i][j], a[i][j] + c * i + c * j)
                ans = min(ans, dp[i][j] + a[i][j] + c * i + c * j)
        a = a[::-1]
    print(ans)

=======
Suggestion 8

def problems210_d():
    h,w,c = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(h)]
    min_a = [[0]*w for _ in range(h)]
    min_a[0][0] = a[0][0]
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                min_a[i][j] = min_a[i][j-1] + c
            elif j == 0:
                min_a[i][j] = min_a[i-1][j] + c
            else:
                min_a[i][j] = min(min_a[i-1][j],min_a[i][j-1]) + c
            min_a[i][j] = min(min_a[i][j],a[i][j])
    min_b = [[0]*w for _ in range(h)]
    min_b[h-1][w-1] = a[h-1][w-1]
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i == h-1 and j == w-1:
                continue
            elif i == h-1:
                min_b[i][j] = min_b[i][j+1] + c
            elif j == w-1:
                min_b[i][j] = min_b[i+1][j] + c
            else:
                min_b[i][j] = min(min_b[i+1][j],min_b[i][j+1]) + c
            min_b[i][j] = min(min_b[i][j],a[i][j])
    min_a_b = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            min_a_b[i][j] = min(min_a[i][j],min_b[i][j])
    ans = 10**18
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                ans = min(ans,min_a_b[i][j]+min_a_b[i][j-1]+c)
            elif j == 0

=======
Suggestion 9

def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    # 1. 从左上角开始，计算以每个点为终点的最小值
    # 2. 从右下角开始，计算以每个点为终点的最小值
    # 3. 两个最小值相加，计算以每个点为终点的最小值，取最小值

    INF = 10 ** 18
    dp1 = [[INF] * w for _ in range(h)]
    dp2 = [[INF] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if i > 0:
                dp1[i][j] = min(dp1[i][j], dp1[i - 1][j])
            if j > 0:
                dp1[i][j] = min(dp1[i][j], dp1[i][j - 1])
            dp1[i][j] = min(dp1[i][j], a[i][j] - c * (i + j))

    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            if i < h - 1:
                dp2[i][j] = min(dp2[i][j], dp2[i + 1][j])
            if j < w - 1:
                dp2[i][j] = min(dp2[i][j], dp2[i][j + 1])
            dp2[i][j] = min(dp2[i][j], a[i][j] - c * (i + j))

    ans = INF
    for i in range(h):
        for j in range(w):
            ans = min(ans, dp1[i][j] + dp2[i][j] + c * (i + j) + a[i][j])

    print(ans)
