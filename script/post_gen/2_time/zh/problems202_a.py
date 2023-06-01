Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    h,w=map(int,input().split())
    a=[input() for _ in range(h)]
    dp=[[0]*w for _ in range(h)]
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            #print(i,j)
            if i==h-1 and j==w-1:
                continue
            if (i+j)%2==0:
                if i==h-1:
                    dp[i][j]=dp[i][j+1]
                    if a[i][j]=='-':
                        dp[i][j]+=1
                elif j==w-1:
                    dp[i][j]=dp[i+1][j]
                    if a[i][j]=='-':
                        dp[i][j]+=1
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
                    if a[i][j]=='-':
                        dp[i][j]+=1
            else:
                if i==h-1:
                    dp[i][j]=dp[i][j+1]
                    if a[i][j]=='+':
                        dp[i][j]+=1
                elif j==w-1:
                    dp[i][j]=dp[i+1][j]
                    if a[i][j]=='+':
                        dp[i][j]+=1
                else:
                    dp[i][j]=min(dp[i+1][j],dp[i][j+1])
                    if a[i][j]=='+':
                        dp[i][j]+=1
    #print(dp)
    if dp[0][0]>0:
        print("Takahashi")
    elif dp[0][0]<0:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 2

def main():
    h,w = map(int,input().split())
    a = [list(input()) for _ in range(h)]
    dp = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i == h-1 and j == w-1:
                continue
            if i == h-1:
                if a[i][j+1] == '+':
                    dp[i][j] = dp[i][j+1]+1
                else:
                    dp[i][j] = dp[i][j+1]-1
            elif j == w-1:
                if a[i+1][j] == '+':
                    dp[i][j] = dp[i+1][j]+1
                else:
                    dp[i][j] = dp[i+1][j]-1
            else:
                if a[i][j+1] == '+':
                    dp[i][j] = max(dp[i][j],dp[i][j+1]+1)
                else:
                    dp[i][j] = max(dp[i][j],dp[i][j+1]-1)
                if a[i+1][j] == '+':
                    dp[i][j] = max(dp[i][j],dp[i+1][j]+1)
                else:
                    dp[i][j] = max(dp[i][j],dp[i+1][j]-1)
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 3

def solve(h, w, a):
    dp = [[0] * (w + 1) for _ in range(h + 1)]
    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            if (i + j) % 2 == 0:
                dp[i][j] = max(dp[i + 1][j] - a[i + 1][j], dp[i][j + 1] - a[i][j + 1])
            else:
                dp[i][j] = max(dp[i + 1][j] + a[i + 1][j], dp[i][j + 1] + a[i][j + 1])
    if dp[0][0] > 0:
        return 'Takahashi'
    elif dp[0][0] < 0:
        return 'Aoki'
    else:
        return 'Draw'


h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
a = [[1 if a[i][j] == '+' else -1 for j in range(w)] for i in range(h)]
print(solve(h, w, a))

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    dp = [[0 for _ in range(w)] for _ in range(h)]
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i == h-1 and j == w-1:
                continue
            if i == h-1:
                if a[i][j+1] == '+':
                    dp[i][j] = dp[i][j+1] + 1
                else:
                    dp[i][j] = dp[i][j+1] - 1
            elif j == w-1:
                if a[i+1][j] == '+':
                    dp[i][j] = dp[i+1][j] + 1
                else:
                    dp[i][j] = dp[i+1][j] - 1
            else:
                if a[i][j+1] == '+':
                    dp[i][j] = dp[i][j+1] + 1
                else:
                    dp[i][j] = dp[i][j+1] - 1
                if a[i+1][j] == '+':
                    dp[i][j] = max(dp[i][j],dp[i+1][j] + 1)
                else:
                    dp[i][j] = max(dp[i][j],dp[i+1][j] - 1)
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 6

def main():
    #读入数据
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    #dp[i][j]表示从i,j开始游戏时，先手的人能得到的最大分数
    dp = [[0] * w for _ in range(h)]
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            if i == h - 1 and j == w - 1:
                continue
            if (i + j) % 2 == 0:
                #先手
                if i == h - 1:
                    dp[i][j] = dp[i][j+1] + (1 if a[i][j+1] == '+' else -1)
                elif j == w - 1:
                    dp[i][j] = dp[i+1][j] + (1 if a[i+1][j] == '+' else -1)
                else:
                    dp[i][j] = max(dp[i][j+1] + (1 if a[i][j+1] == '+' else -1), dp[i+1][j] + (1 if a[i+1][j] == '+' else -1))
            else:
                #后手
                if i == h - 1:
                    dp[i][j] = dp[i][j+1] - (1 if a[i][j+1] == '+' else -1)
                elif j == w - 1:
                    dp[i][j] = dp[i+1][j] - (1 if a[i+1][j] == '+' else -1)
                else:
                    dp[i][j] = min(dp[i][j+1] - (1 if a[i][j+1] == '+' else -1), dp[i+1][j] - (1 if a[i+1][j] == '+' else -1))
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 7

def main():
    h, w = map(int, input().split())
    a = [list(input()) for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            if i == h - 1 and j == w - 1: continue
            if (i + j) % 2 == 0:
                dp[i][j] = -float('inf')
                if i + 1 < h:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j] + (1 if a[i + 1][j] == '+' else -1))
                if j + 1 < w:
                    dp[i][j] = max(dp[i][j], dp[i][j + 1] + (1 if a[i][j + 1] == '+' else -1))
            else:
                dp[i][j] = float('inf')
                if i + 1 < h:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] - (1 if a[i + 1][j] == '+' else -1))
                if j + 1 < w:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] - (1 if a[i][j + 1] == '+' else -1))
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 8

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            if (i + j) % 2 == 0:
                if i == h - 1 and j == w - 1:
                    continue
                if i == h - 1:
                    dp[i][j] = dp[i][j + 1]
                elif j == w - 1:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                if a[i][j] == '+':
                    dp[i][j] += 1
                else:
                    dp[i][j] -= 1
            else:
                if i == h - 1 and j == w - 1:
                    continue
                if i == h - 1:
                    dp[i][j] = dp[i][j + 1]
                elif j == w - 1:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = min(dp[i + 1][j], dp[i][j + 1])
                if a[i][j] == '+':
                    dp[i][j] -= 1
                else:
                    dp[i][j] += 1
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')
