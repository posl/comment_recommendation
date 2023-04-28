Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    for h in range(H - 1, -1, -1):
        for w in range(W - 1, -1, -1):
            dp[h][w] = max(dp[h + 1][w] + (1 if A[h][w] == '+' else -1), dp[h][w + 1] + (1 if A[h][w] == '+' else -1))
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 2

def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    for i in range(H):
        for j in range(W):
            dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] - dp[i][j]
            if A[i][j] == '+':
                dp[i + 1][j + 1] += 1
            else:
                dp[i + 1][j + 1] -= 1
    if dp[H][W] == 0:
        print('Draw')
    elif dp[H][W] > 0:
        print('Takahashi')
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
            if i == 0 and j == 0:
                dp[i][j] = 1 if A[i][j] == '+' else -1
            elif i == 0:
                dp[i][j] = dp[i][j - 1] * (-1) if A[i][j] == '+' else dp[i][j - 1] * (-1) - 1
            elif j == 0:
                dp[i][j] = dp[i - 1][j] * (-1) if A[i][j] == '+' else dp[i - 1][j] * (-1) - 1
            else:
                dp[i][j] = max(dp[i - 1][j] * (-1) if A[i][j] == '+' else dp[i - 1][j] * (-1) - 1,
                               dp[i][j - 1] * (-1) if A[i][j] == '+' else dp[i][j - 1] * (-1) - 1)
    if dp[H - 1][W - 1] == 0:
        print('Draw')
    elif dp[H - 1][W - 1] > 0:
        print('Takahashi')
    else:
        print('Aoki')

=======
Suggestion 4

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1 if A[0][0] == '+' else -1
    for i in range(1, H):
        if A[i][0] == '+':
            dp[i][0] = dp[i - 1][0] + 1
        else:
            dp[i][0] = dp[i - 1][0] - 1
    for j in range(1, W):
        if A[0][j] == '+':
            dp[0][j] = dp[0][j - 1] + 1
        else:
            dp[0][j] = dp[0][j - 1] - 1

    for i in range(1, H):
        for j in range(1, W):
            if A[i][j] == '+':
                dp[i][j] = max(dp[i - 1][j] + 1, dp[i][j - 1] + 1)
            else:
                dp[i][j] = min(dp[i - 1][j] - 1, dp[i][j - 1] - 1)

    if dp[-1][-1] > 0:
        print('Takahashi')
    elif dp[-1][-1] < 0:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 5

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                dp[i][j] = 1 if a[i][j] == '+' else -1
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + 1 if a[i][j] == '+' else dp[i][j - 1] - 1
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + 1 if a[i][j] == '+' else dp[i - 1][j] - 1
            else:
                dp[i][j] = max(dp[i - 1][j] + 1 if a[i][j] == '+' else dp[i - 1][j] - 1, dp[i][j - 1] + 1 if a[i][j] == '+' else dp[i][j - 1] - 1)
    if dp[h - 1][w - 1] > 0:
        print('Takahashi')
    elif dp[h - 1][w - 1] < 0:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1 if a[0][0] == '+' else -1
    for i in range(h):
        for j in range(w):
            if i == j == 0:
                continue
            if (i + j) % 2 == 0:
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + (1 if a[i][j] == '+' else -1)
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + (1 if a[i][j] == '+' else -1)
                else:
                    dp[i][j] = max(dp[i][j - 1] + (1 if a[i][j] == '+' else -1), dp[i - 1][j] + (1 if a[i][j] == '+' else -1))
            else:
                if i == 0:
                    dp[i][j] = dp[i][j - 1] - (1 if a[i][j] == '+' else -1)
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] - (1 if a[i][j] == '+' else -1)
                else:
                    dp[i][j] = min(dp[i][j - 1] - (1 if a[i][j] == '+' else -1), dp[i - 1][j] - (1 if a[i][j] == '+' else -1))
    if dp[-1][-1] > 0:
        print('Takahashi')
    elif dp[-1][-1] < 0:
        print('Aoki')
    else:
        print('Draw')

main()

=======
Suggestion 7

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if (h + w) % 2 == 0:
                if h == 0 and w == 0:
                    dp[h][w] = 1 if A[h][w] == '+' else -1
                elif h == 0:
                    dp[h][w] = dp[h][w - 1] + 1 if A[h][w] == '+' else dp[h][w - 1] - 1
                elif w == 0:
                    dp[h][w] = dp[h - 1][w] + 1 if A[h][w] == '+' else dp[h - 1][w] - 1
                else:
                    dp[h][w] = max(dp[h - 1][w] + 1 if A[h][w] == '+' else dp[h - 1][w] - 1,
                                   dp[h][w - 1] + 1 if A[h][w] == '+' else dp[h][w - 1] - 1)
            else:
                if h == 0 and w == 0:
                    dp[h][w] = -1 if A[h][w] == '+' else 1
                elif h == 0:
                    dp[h][w] = dp[h][w - 1] - 1 if A[h][w] == '+' else dp[h][w - 1] + 1
                elif w == 0:
                    dp[h][w] = dp[h - 1][w] - 1 if A[h][w] == '+' else dp[h - 1][w] + 1
                else:
                    dp[h][w] = min(dp[h - 1][w] - 1 if A[h][w] == '+' else dp[h - 1][w] + 1,
                                   dp[h][w - 1] - 1 if A[h][w] == '+' else dp[h][w - 1] + 1)
    if dp[H - 1][W - 1] > 0:
        print('Takahashi')
    elif dp

=======
Suggestion 8

def solve():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1 if A[0][0] == '+' else -1
    for i in range(H):
        for j in range(W):
            if i == j == 0:
                continue
            if (i + j) % 2 == 0:
                dp[i][j] = max(dp[i - 1][j] + (1 if A[i][j] == '+' else -1), dp[i][j - 1] + (1 if A[i][j] == '+' else -1))
            else:
                dp[i][j] = min(dp[i - 1][j] - (1 if A[i][j] == '+' else -1), dp[i][j - 1] - (1 if A[i][j] == '+' else -1))
    if dp[H - 1][W - 1] > 0:
        print('Takahashi')
    elif dp[H - 1][W - 1] < 0:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 9

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]

    dp = [[0] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + (1 if A[i][j] == "+" else -1)) if i > 0 else 0
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + (1 if A[i][j] == "+" else -1)) if j > 0 else 0
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] - (1 if A[i][j] == "+" else -1)) if i > 0 else 0
                dp[i][j] = min(dp[i][j], dp[i][j - 1] - (1 if A[i][j] == "+" else -1)) if j > 0 else 0

    if dp[H - 1][W - 1] > 0:
        print("Takahashi")
    elif dp[H - 1][W - 1] == 0:
        print("Draw")
    else:
        print("Aoki")

=======
Suggestion 10

def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    dp = [[0] * w for _ in range(h)]
    dp[0][0] = 1 if a[0][0] == "+" else -1
    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if (i + j) % 2 == 0:
                if i == 0:
                    dp[i][j] = dp[i][j - 1] + (1 if a[i][j] == "+" else -1)
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + (1 if a[i][j] == "+" else -1)
                else:
                    dp[i][j] = max(dp[i][j - 1] + (1 if a[i][j] == "+" else -1), dp[i - 1][j] + (1 if a[i][j] == "+" else -1))
            else:
                if i == 0:
                    dp[i][j] = dp[i][j - 1] - (1 if a[i][j] == "+" else -1)
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] - (1 if a[i][j] == "+" else -1)
                else:
                    dp[i][j] = min(dp[i][j - 1] - (1 if a[i][j] == "+" else -1), dp[i - 1][j] - (1 if a[i][j] == "+" else -1))
    if dp[h - 1][w - 1] > 0:
        print("Takahashi")
    elif dp[h - 1][w - 1] < 0:
        print("Aoki")
    else:
        print("Draw")
