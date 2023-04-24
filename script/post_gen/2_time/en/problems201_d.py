Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    for h in range(H):
        for w in range(W):
            if (h + w) % 2 == 0:
                dp[h + 1][w + 1] = max(dp[h][w + 1] + 1 if A[h][w] == "+" else dp[h][w + 1] - 1,
                                       dp[h + 1][w] + 1 if A[h][w] == "+" else dp[h + 1][w] - 1)
            else:
                dp[h + 1][w + 1] = min(dp[h][w + 1] + 1 if A[h][w] == "+" else dp[h][w + 1] - 1,
                                       dp[h + 1][w] + 1 if A[h][w] == "+" else dp[h + 1][w] - 1)
    print("Takahashi" if dp[H][W] > 0 else "Aoki" if dp[H][W] < 0 else "Draw")

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if (i + j) % 2 == 0:
                dp[i][j] = max(dp[i + 1][j] + (1 if A[i][j] == '+' else -1), dp[i][j + 1] + (1 if A[i][j] == '+' else -1))
            else:
                dp[i][j] = min(dp[i + 1][j] - (1 if A[i][j] == '+' else -1), dp[i][j + 1] - (1 if A[i][j] == '+' else -1))
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] == 0:
        print('Draw')
    else:
        print('Aoki')

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if A[i][j] == '+':
                dp[i][j] = 1
            else:
                dp[i][j] = -1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            if i == 0:
                dp[i][j] += dp[i][j-1]
            elif j == 0:
                dp[i][j] += dp[i-1][j]
            else:
                dp[i][j] += max(dp[i-1][j], dp[i][j-1])
    if dp[H-1][W-1] > 0:
        print("Takahashi")
    elif dp[H-1][W-1] < 0:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 0:
                if i == 0 and j == 0:
                    if A[i][j] == '+':
                        dp[i][j] = 1
                    else:
                        dp[i][j] = -1
                elif i == 0:
                    if A[i][j] == '+':
                        dp[i][j] = dp[i][j - 1] + 1
                    else:
                        dp[i][j] = dp[i][j - 1] - 1
                elif j == 0:
                    if A[i][j] == '+':
                        dp[i][j] = dp[i - 1][j] + 1
                    else:
                        dp[i][j] = dp[i - 1][j] - 1
                else:
                    if A[i][j] == '+':
                        dp[i][j] = max(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                    else:
                        dp[i][j] = min(dp[i - 1][j] - 1, dp[i][j - 1] - 1)
            else:
                if i == 0 and j == 0:
                    if A[i][j] == '+':
                        dp[i][j] = -1
                    else:
                        dp[i][j] = 1
                elif i == 0:
                    if A[i][j] == '+':
                        dp[i][j] = dp[i][j - 1] - 1
                    else:
                        dp[i][j] = dp[i][j - 1] + 1
                elif j == 0:
                    if A[i][j] == '+':
                        dp[i][j] = dp[i - 1][j] - 1
                    else:
                        dp[i][j] = dp[i - 1][j] + 1
                else:
                    if A[i][j] == '+':
                        dp[i][j] = min(dp[i - 1][

=======
Suggestion 5

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1 if A[0][0] == "+" else -1
    for i in range(H):
        for j in range(W):
            if i == j == 0:
                continue
            if (i + j) % 2 == 0:
                if i > 0 and j > 0:
                    dp[i][j] = max(dp[i - 1][j] + (1 if A[i][j] == "+" else -1), dp[i][j - 1] + (1 if A[i][j] == "+" else -1))
                elif i > 0:
                    dp[i][j] = dp[i - 1][j] + (1 if A[i][j] == "+" else -1)
                else:
                    dp[i][j] = dp[i][j - 1] + (1 if A[i][j] == "+" else -1)
            else:
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j] - (1 if A[i][j] == "+" else -1), dp[i][j - 1] - (1 if A[i][j] == "+" else -1))
                elif i > 0:
                    dp[i][j] = dp[i - 1][j] - (1 if A[i][j] == "+" else -1)
                else:
                    dp[i][j] = dp[i][j - 1] - (1 if A[i][j] == "+" else -1)
    if dp[H - 1][W - 1] > 0:
        print("Takahashi")
    elif dp[H - 1][W - 1] < 0:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 6

def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                dp[i][j] = 1 if A[i][j] == "+" else -1
            elif i == 0:
                dp[i][j] = dp[i][j - 1] * (-1) if A[i][j] == "-" else dp[i][j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] * (-1) if A[i][j] == "-" else dp[i - 1][j]
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j] * (-1) if A[i][j] == "-" else dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1] * (-1) if A[i][j] == "-" else dp[i][j - 1]
    print("Takahashi" if dp[H - 1][W - 1] > 0 else "Aoki" if dp[H - 1][W - 1] < 0 else "Draw")

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * (W+1) for _ in range(H+1)]
    for h in range(H):
        for w in range(W):
            if (h + w) % 2 == 0:
                dp[h+1][w+1] = max(dp[h][w+1] + (1 if A[h][w] == "+" else -1), dp[h+1][w] + (1 if A[h][w] == "+" else -1))
            else:
                dp[h+1][w+1] = min(dp[h][w+1] - (1 if A[h][w] == "+" else -1), dp[h+1][w] - (1 if A[h][w] == "+" else -1))
    if dp[H][W] > 0:
        print("Takahashi")
    elif dp[H][W] < 0:
        print("Aoki")
    else:
        print("Draw")

=======
Suggestion 8

def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    for h in range(H - 1, -1, -1):
        for w in range(W - 1, -1, -1):
            if (h + w) % 2 == 0:
                if a[h][w] == '+':
                    dp[h][w] = max(dp[h][w], dp[h + 1][w] + 1)
                    dp[h][w] = max(dp[h][w], dp[h][w + 1] + 1)
                else:
                    dp[h][w] = max(dp[h][w], dp[h + 1][w] - 1)
                    dp[h][w] = max(dp[h][w], dp[h][w + 1] - 1)
            else:
                if a[h][w] == '+':
                    dp[h][w] = min(dp[h][w], dp[h + 1][w] - 1)
                    dp[h][w] = min(dp[h][w], dp[h][w + 1] - 1)
                else:
                    dp[h][w] = min(dp[h][w], dp[h + 1][w] + 1)
                    dp[h][w] = min(dp[h][w], dp[h][w + 1] + 1)
    if dp[0][0] == 0:
        print('Draw')
    elif dp[0][0] > 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(input()))
    dp = [[0] * W for i in range(H)]
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                dp[i][j] = 1 if A[i][j] == '+' else -1
            elif i == 0:
                dp[i][j] = dp[i][j - 1] * (-1) if A[i][j] == '+' else dp[i][j - 1]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] * (-1) if A[i][j] == '+' else dp[i - 1][j]
            else:
                if A[i][j] == '+':
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
    if dp[H - 1][W - 1] > 0:
        print('Takahashi')
    elif dp[H - 1][W - 1] < 0:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 10

def main():
    H,W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0]*(W+1) for _ in range(H+1)]
    for i in range(H-1,-1,-1):
        for j in range(W-1,-1,-1):
            if (i+j)%2==0:
                dp[i][j] = max(dp[i+1][j] + int(A[i][j]=='-'), dp[i][j+1] + int(A[i][j]=='-'))
            else:
                dp[i][j] = min(dp[i+1][j] - int(A[i][j]=='+'), dp[i][j+1] - int(A[i][j]=='+'))
    if dp[0][0]>0:
        print('Takahashi')
    elif dp[0][0]<0:
        print('Aoki')
    else:
        print('Draw')
