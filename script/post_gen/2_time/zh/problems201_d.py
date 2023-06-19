Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    print('Hello World!')

=======
Suggestion 3

def readinput():
    h,w=map(int,input().split())
    a=[]
    for _ in range(h):
        a.append(input())
    return h,w,a

=======
Suggestion 4

def main():
    print("hello world!")

=======
Suggestion 5

def main():
    h,w=map(int,input().split())
    a=[input() for i in range(h)]
    dp=[[0]*w for i in range(h)]
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i==h-1 and j==w-1:
                continue
            if (i+j)%2==0:
                if i==h-1:
                    dp[i][j]=dp[i][j+1]
                elif j==w-1:
                    dp[i][j]=dp[i+1][j]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
                if a[i][j]=="+":
                    dp[i][j]+=1
                else:
                    dp[i][j]-=1
            else:
                if i==h-1:
                    dp[i][j]=dp[i][j+1]
                elif j==w-1:
                    dp[i][j]=dp[i+1][j]
                else:
                    dp[i][j]=min(dp[i+1][j],dp[i][j+1])
                if a[i][j]=="+":
                    dp[i][j]-=1
                else:
                    dp[i][j]+=1
    if dp[0][0]>0:
        print("Takahashi")
    elif dp[0][0]<0:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 6

def main():
    #输入
    H,W = map(int,input().split())
    A = []
    for i in range(H):
        A.append(list(input()))

    #动态规划
    dp = [[0 for i in range(W)] for j in range(H)]
    dp[H-1][W-1] = 0
    for i in range(H-1,-1,-1):
        for j in range(W-1,-1,-1):
            if i == H-1 and j == W-1:
                continue
            elif i == H-1:
                if A[i][j] == "+":
                    dp[i][j] = dp[i][j+1]-1
                else:
                    dp[i][j] = dp[i][j+1]+1
            elif j == W-1:
                if A[i][j] == "+":
                    dp[i][j] = dp[i+1][j]-1
                else:
                    dp[i][j] = dp[i+1][j]+1
            else:
                if A[i][j] == "+":
                    dp[i][j] = max(dp[i+1][j]-1,dp[i][j+1]-1)
                else:
                    dp[i][j] = min(dp[i+1][j]+1,dp[i][j+1]+1)

    #判断
    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] < 0:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 7

def main():
    # 读取输入
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    # dp[i][j]表示从(i,j)到达(h-1,w-1)的最大分数差
    dp = [[0]*w for _ in range(h)]
    # 从后往前
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            # 如果是最后一个元素
            if i == h-1 and j == w-1:
                continue
            # 如果是最后一行
            if i == h-1:
                if a[i][j] == '+':
                    dp[i][j] = dp[i][j+1]
                else:
                    dp[i][j] = dp[i][j+1] - 1
            # 如果是最后一列
            elif j == w-1:
                if a[i][j] == '+':
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] - 1
            # 如果不是最后一行或最后一列
            else:
                if a[i][j] == '+':
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j]) - 1
    # 输出结果
    if dp[0][0] == 0:
        print('Draw')
    elif dp[0][0] > 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 8

def main():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    dp = [[0]*w for _ in range(h)]
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i == h-1 and j == w-1:
                continue
            if (i+j)%2 == 0:
                dp[i][j] = max(dp[i+1][j],dp[i][j+1])
                if a[i][j] == '+':
                    dp[i][j] += 1
                else:
                    dp[i][j] -= 1
            else:
                dp[i][j] = min(dp[i+1][j],dp[i][j+1])
                if a[i][j] == '+':
                    dp[i][j] -= 1
                else:
                    dp[i][j] += 1
    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] == 0:
        print("Draw")
    else:
        print("Aoki")

=======
Suggestion 9

def main():
    h,w = map(int, input().split())
    a = [input() for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            if i == h-1 and j == w-1:
                continue
            if i == h-1:
                if a[i][j+1] == '+':
                    dp[i][j] = -dp[i][j+1] + 1
                else:
                    dp[i][j] = -dp[i][j+1] - 1
            elif j == w-1:
                if a[i+1][j] == '+':
                    dp[i][j] = -dp[i+1][j] + 1
                else:
                    dp[i][j] = -dp[i+1][j] - 1
            else:
                if a[i][j+1] == '+':
                    dp[i][j] = max(-dp[i][j+1] + 1, -dp[i+1][j])
                else:
                    dp[i][j] = max(-dp[i][j+1] - 1, -dp[i+1][j])
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')
