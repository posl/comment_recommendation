Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0]*W for _ in range(H)]
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            if i == H-1 and j == W-1:
                continue
            if i == H-1:
                if A[i][j+1] == '+':
                    dp[i][j] = dp[i][j+1] - 1
                else:
                    dp[i][j] = dp[i][j+1] + 1
            elif j == W-1:
                if A[i+1][j] == '+':
                    dp[i][j] = dp[i+1][j] - 1
                else:
                    dp[i][j] = dp[i+1][j] + 1
            else:
                if A[i][j+1] == '+':
                    dp[i][j] = min(dp[i][j+1] - 1, dp[i+1][j])
                else:
                    dp[i][j] = max(dp[i][j+1] + 1, dp[i+1][j])
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 2

def main():
    H,W = map(int,input().split())
    A = [input() for i in range(H)]
    #print(H,W)
    #print(A)
    #print(A[0][0])
    #print(A[0][1])
    #print(A[1][0])
    #print(A[1][1])
    #print(A[2][0])
    #print(A[2][1])
    #print(A[3][0])
    #print(A[3][1])
    #print(A[4][0])
    #print(A[4][1])
    #print(A[5][0])
    #print(A[5][1])
    #print(A[6][0])
    #print(A[6][1])
    #print(A[7][0])
    #print(A[7][1])
    #print(A[8][0])
    #print(A[8][1])
    #print(A[9][0])
    #print(A[9][1])
    #print(A[10][0])
    #print(A[10][1])
    #print(A[11][0])
    #print(A[11][1])
    #print(A[12][0])
    #print(A[12][1])
    #print(A[13][0])
    #print(A[13][1])
    #print(A[14][0])
    #print(A[14][1])
    #print(A[15][0])
    #print(A[15][1])
    #print(A[16][0])
    #print(A[16][1])
    #print(A[17][0])
    #print(A[17][1])
    #print(A[18][0])
    #print(A[18][1])
    #print(A[19][0])
    #print(A[19][1])
    #print(A[20][0])
    #print(A[20][1])
    #print(A[21][0])
    #print(A[21][1])
    #print(A[22][0])
    #print(A[22][1])
    #print(A[23][0])
    #print(A[23][1])
    #print(A[24][0])
    #print(A[24][1])
    #print(A[25][0])
    #print(A[25

=======
Suggestion 3

def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    # 2次元配列の初期化
    dp = [[0] * W for _ in range(H)]

    # 配列の最後の要素から逆順にループ
    for i in range(H-1, -1, -1):
        for j in range(W-1, -1, -1):
            # 配列の最後の要素だけは別処理
            if i == H-1 and j == W-1:
                continue

            # 配列の最後の行は、右にしか移動できない
            if i == H-1:
                # 青マスなら+1, 赤マスなら-1
                dp[i][j] = dp[i][j+1] + 1 if A[i][j+1] == "+" else dp[i][j+1] - 1
            # 配列の最後の列は、下にしか移動できない
            elif j == W-1:
                # 青マスなら+1, 赤マスなら-1
                dp[i][j] = dp[i+1][j] + 1 if A[i+1][j] == "+" else dp[i+1][j] - 1
            # 配列の最後の行と列以外は、右と下のどちらかに移動する
            else:
                # 青マスなら+1, 赤マスなら-1
                dp[i][j] = max(dp[i+1][j] + 1 if A[i+1][j] == "+" else dp[i+1][j] - 1, dp[i][j+1] + 1 if A[i][j+1] == "+" else dp[i][j+1] - 1)

    # 配列の最初の要素の値で判定
    if dp[0][0] > 0:
        print("Takahashi")
    elif dp[0][0] < 0:

=======
Suggestion 4

def main():
    h,w = map(int,input().split())
    a = [input() for i in range(h)]
    #print(a)
    dp = [[0 for i in range(w)] for j in range(h)]
    dp[-1][-1] = 1 if a[-1][-1] == '+' else -1
    for i in range(h-2,-1,-1):
        if a[i][-1] == '+':
            dp[i][-1] = dp[i+1][-1] - 1
        else:
            dp[i][-1] = dp[i+1][-1] + 1
    for i in range(w-2,-1,-1):
        if a[-1][i] == '+':
            dp[-1][i] = dp[-1][i+1] - 1
        else:
            dp[-1][i] = dp[-1][i+1] + 1
    #print(dp)
    for i in range(h-2,-1,-1):
        for j in range(w-2,-1,-1):
            if a[i][j] == '+':
                dp[i][j] = max(dp[i+1][j] - 1, dp[i][j+1] - 1)
            else:
                dp[i][j] = min(dp[i+1][j] + 1, dp[i][j+1] + 1)
    #print(dp)
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')

=======
Suggestion 5

def main():
    # 標準入力の取得
    H, W = map(int, input().split())
    A = [input() for i in range(H)]

    # 処理
    # どちらが勝つかを判定する
    # どちらが勝つかは、青の数が多い方が勝つ
    # どちらが勝つかは、青の数が多い方が勝つ
    # どちらが勝つかは、青の数が多い方が勝つ
    # どちらが勝つかは、青の数が多い方が勝つ
    # どちらが勝つかは、青の数が多い方が勝つ
    # どちらが勝つかは、青の数が多い方が勝つ
    # どちらが勝つかは、青の数が多い方が勝つ
    # どちらが勝つかは、青の数が多い方が勝つ
    # どちらが勝つかは、青の数が多い方が勝つ

    # 標準出力への書き出し
    print(ans)

=======
Suggestion 6

def main():
    h, w = map(int, input().split())
    a = [list(input()) for i in range(h)]
    #print(a)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[0][0] == '+')
    #print(a[0][0] == '-')
    #print(a[1][0] == '+')
    #print(a[1][0] == '-')
    #print(a[0][1] == '+')
    #print(a[0][1] == '-')
    #print(a[1][1] == '+')
    #print(a[1][1] == '-')
    #print(a[0][0] == '+')
    #print(a[0][0] == '-')
    #print(a[1][0] == '+')
    #print(a[1][0] == '-')
    #print(a[0][1] == '+')
    #print(a[0][1] == '-')
    #print(a[1][1] == '+')
    #print(a[1][1] == '-')

    #print(a[0][0] == '+')
    #print(a[0][0] == '-')
    #print(a[1][0] == '+')
    #print(a[1][0] == '-')
    #print(a[0][1] == '+')
    #print(a[0][1] == '-')
    #print(a[1][1] == '+')
    #print(a[1][1] == '-')
    #print(a[0][0] == '+')
    #print(a[0][0] == '-')
    #print(a[1][0] == '+')
    #print(a[1][0] == '-')
    #print(a[0][1] == '+')
    #print(a[0][1] == '-')
    #print(a[1][1] == '+')
    #print(a[1][1] == '-')
    #print(a[0][0] == '+')
    #print(a[0][0] == '-')
    #print(a[1][0] == '+')
    #print(a[1][0] == '-')
    #print(a[0][1] == '+')
    #print(a[

=======
Suggestion 7

def main():
    H,W = map(int,input().split())
    A = [input() for _ in range(H)]
    #print(A)
    #print(A[0][0])
    #print(A[0][1])
    #print(A[1][0])
    #print(A[1][1])
    #print(A[2][0])
    #print(A[2][1])
    #print(A[3][0])
    #print(A[3][1])
    #print(A[4][0])
    #print(A[4][1])
    #print(A[5][0])
    #print(A[5][1])
    #print(A[6][0])
    #print(A[6][1])
    #print(A[7][0])
    #print(A[7][1])
    #print(A[8][0])
    #print(A[8][1])
    #print(A[9][0])
    #print(A[9][1])
    #print(A[10][0])
    #print(A[10][1])
    #print(A[11][0])
    #print(A[11][1])
    #print(A[12][0])
    #print(A[12][1])
    #print(A[13][0])
    #print(A[13][1])
    #print(A[14][0])
    #print(A[14][1])
    #print(A[15][0])
    #print(A[15][1])
    #print(A[16][0])
    #print(A[16][1])
    #print(A[17][0])
    #print(A[17][1])
    #print(A[18][0])
    #print(A[18][1])
    #print(A[19][0])
    #print(A[19][1])
    #print(A[20][0])
    #print(A[20][1])
    #print(A[21][0])
    #print(A[21][1])
    #print(A[22][0])
    #print(A[22][1])
    #print(A[23][0])
    #print(A[23][1])
    #print(A[24][0])
    #print(A[24][1])
    #print(A[25][0])
    #print(A[25][1])
    #print

=======
Suggestion 8

def main():
    h,w = map(int,input().split())
    a = [input() for _ in range(h)]
    #print(a)
    #print(a[0][1])
    #print(a[0][2])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[2][2])

    #print(a[0][0])
    #print(a[1][0])
    #print(a[2][0])
    #print(a[0][1])
    #print(a[1][1])
    #print(a[2][1])
    #print(a[0][2])
    #print(a[1][2])
    #print(a[2][2])

    #print(a[0][0])
    #print(a[0][1])
    #print(a[0][2])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[2][2])

    #print(a[0][0])
    #print(a[1][0])
    #print(a[2][0])
    #print(a[0][1])
    #print(a[1][1])
    #print(a[2][1])
    #print(a[0][2])
    #print(a[1][2])
    #print(a[2][2])

    #print(a[0][0])
    #print(a[1][0])
    #print(a[2][0])
    #print(a[0][1])
    #print(a[1][1])
    #print(a[2][1])
    #print(a[0][2])
    #print(a[1][2])
    #print(a[2][2])

    #print(a[0][0])
    #print(a[1][0])
    #print(a[2][0])
    #print(a[0][1])
    #print(a[1][1])
    #print(a[2][1])
    #print(a[0][2])
    #print(a[1][2])
    #print

=======
Suggestion 9

def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(list(input()))
    #print(a)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[0][2])
    #print(a[1][2])
    #print(a[2][2])
    #print(a[0][0])
    #print(a[1][0])
    #print(a[2][0])
    #print(a[0][1])
    #print(a[1][1])
    #print(a[2][1])
    #print(a[0][2])
    #print(a[1][2])
    #print(a[2][2])
    #print(a[0][0])
    #print(a[0][1])
    #print(a[0][2])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[2][2])
    #print(a[0][0])
    #print(a[0][1])
    #print(a[0][2])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[2][2])
    #print(a[0][0])
    #print(a[0][1])
    #print(a[0][2])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[2][2])
    #print(a[0][0])
    #print(a[0][1])
    #print(a[0][2])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[1][2])
    #print(a[2][

=======
Suggestion 10

def main():
    h,w = map(int,input().split())
    a = [input() for i in range(h)]
    dp = [[0 for i in range(w)] for j in range(h)]
    for i in range(h-1,-1,-1):
        for j in range(w-1,-1,-1):
            if i == h-1 and j == w-1:
                continue
            if i == h-1:
                if a[i][j+1] == '+':
                    dp[i][j] = dp[i][j+1] - 1
                else:
                    dp[i][j] = dp[i][j+1] + 1
            elif j == w-1:
                if a[i+1][j] == '+':
                    dp[i][j] = dp[i+1][j] - 1
                else:
                    dp[i][j] = dp[i+1][j] + 1
            else:
                if a[i][j+1] == '+':
                    dp[i][j] = min(dp[i][j+1] - 1, dp[i+1][j])
                else:
                    dp[i][j] = min(dp[i][j+1] + 1, dp[i+1][j])
    if dp[0][0] > 0:
        print('Takahashi')
    elif dp[0][0] < 0:
        print('Aoki')
    else:
        print('Draw')
