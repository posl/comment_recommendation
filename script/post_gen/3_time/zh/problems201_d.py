Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    print("hello world!")

=======
Suggestion 3

def main():
    h,w = map(int,input().split())
    a = [list(input()) for _ in range(h)]
    dp = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h)[::-1]:
        for j in range(w)[::-1]:
            if i == h-1 and j == w-1:
                continue
            if (i+j)%2 == 0:
                dp[i][j] = -float('inf')
                if i+1 < h:
                    dp[i][j] = max(dp[i][j],dp[i+1][j]+(1 if a[i+1][j] == '+' else -1))
                if j+1 < w:
                    dp[i][j] = max(dp[i][j],dp[i][j+1]+(1 if a[i][j+1] == '+' else -1))
            else:
                dp[i][j] = float('inf')
                if i+1 < h:
                    dp[i][j] = min(dp[i][j],dp[i+1][j]-(1 if a[i+1][j] == '+' else -1))
                if j+1 < w:
                    dp[i][j] = min(dp[i][j],dp[i][j+1]-(1 if a[i][j+1] == '+' else -1))
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] == 0:
        print('Draw')
    else:
        print('Aoki')

=======
Suggestion 4

def main():
    h,w = map(int,input().split())
    a = [list(input()) for i in range(h)]
    dp = [[0 for i in range(w)] for j in range(h)]
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i == h-1 and j == w-1:
                continue
            if i == h-1:
                if a[i][j+1] == "+":
                    dp[i][j] = dp[i][j+1] + 1
                else:
                    dp[i][j] = dp[i][j+1] - 1
            elif j == w-1:
                if a[i+1][j] == "+":
                    dp[i][j] = dp[i+1][j] + 1
                else:
                    dp[i][j] = dp[i+1][j] - 1
            else:
                if a[i][j+1] == "+":
                    dp[i][j] = max(dp[i][j],dp[i][j+1] + 1)
                else:
                    dp[i][j] = max(dp[i][j],dp[i][j+1] - 1)
                if a[i+1][j] == "+":
                    dp[i][j] = max(dp[i][j],dp[i+1][j] + 1)
                else:
                    dp[i][j] = max(dp[i][j],dp[i+1][j] - 1)
    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] < 0:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 5

def main():
    H,W = map(int,input().split())
    A = [list(input()) for i in range(H)]
    dp = [[0]*W for i in range(H)]
    for i in range(H-1,-1,-1):
        for j in range(W-1,-1,-1):
            if i == H-1 and j == W-1:
                dp[i][j] = 0
            elif i == H-1:
                if A[i][j+1] == "+":
                    dp[i][j] = dp[i][j+1] + 1
                else:
                    dp[i][j] = dp[i][j+1] - 1
            elif j == W-1:
                if A[i+1][j] == "+":
                    dp[i][j] = dp[i+1][j] + 1
                else:
                    dp[i][j] = dp[i+1][j] - 1
            else:
                if A[i][j+1] == "+":
                    dp[i][j] = max(dp[i][j+1] + 1,dp[i+1][j])
                else:
                    dp[i][j] = min(dp[i][j+1] - 1,dp[i+1][j])
    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] < 0:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 6

def main():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    dp = [[0]*w for _ in range(h)]
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i == h-1 and j == w-1:
                continue
            if i == h-1:
                if a[i][j] == '+':
                    dp[i][j] = dp[i][j+1]-1
                else:
                    dp[i][j] = dp[i][j+1]+1
            elif j == w-1:
                if a[i][j] == '+':
                    dp[i][j] = dp[i+1][j]-1
                else:
                    dp[i][j] = dp[i+1][j]+1
            else:
                if a[i][j] == '+':
                    dp[i][j] = min(dp[i+1][j]-1,dp[i][j+1]-1)
                else:
                    dp[i][j] = min(dp[i+1][j]+1,dp[i][j+1]+1)
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 7

def main():
    print("Hello World!")
    return

=======
Suggestion 8

def main():
    # 读入
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]

    # 从下往上、从右往左依次计算
    dp = [[0] * w for _ in range(h)]
    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            # 如果是最后一个，就是自己的得分
            if i == h - 1 and j == w - 1:
                continue
            # 如果是红色，就是对方的得分
            if (i + j) % 2 == 1:
                dp[i][j] = 10 ** 10
                if i + 1 < h:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + (1 if a[i + 1][j] == '-' else -1))
                if j + 1 < w:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + (1 if a[i][j + 1] == '-' else -1))
            # 如果是蓝色，就是自己的得分
            else:
                dp[i][j] = -10 ** 10
                if i + 1 < h:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j] - (1 if a[i + 1][j] == '-' else -1))
                if j + 1 < w:
                    dp[i][j] = max(dp[i][j], dp[i][j + 1] - (1 if a[i][j + 1] == '-' else -1))

    # 判断结果
    if dp[0][0] == 0:
        print("Draw")
    elif dp[0][0] > 0:
        print("Takahashi")
    else:
        print("Aoki")

=======
Suggestion 9

def main():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    dp = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i == h-1 and j == w-1:
                continue
            if (i+j)%2 == 0:
                if i == h-1:
                    dp[i][j] = dp[i][j+1] + (1 if a[i][j] == '+' else -1)
                elif j == w-1:
                    dp[i][j] = dp[i+1][j] + (1 if a[i][j] == '+' else -1)
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1]) + (1 if a[i][j] == '+' else -1)
            else:
                if i == h-1:
                    dp[i][j] = dp[i][j+1] - (1 if a[i][j] == '+' else -1)
                elif j == w-1:
                    dp[i][j] = dp[i+1][j] - (1 if a[i][j] == '+' else -1)
                else:
                    dp[i][j] = min(dp[i+1][j],dp[i][j+1]) - (1 if a[i][j] == '+' else -1)
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] == 0:
        print('Draw')
    else:
        print('Aoki')
