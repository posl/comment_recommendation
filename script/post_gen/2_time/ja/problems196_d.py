Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, W, A, B = map(int, input().split())
    print(solve(H, W, A, B))

=======
Suggestion 2

def main():
    H, W, A, B = map(int, input().split())
    HW = H * W
    ans = 0
    for i in range(1 << HW):
        a = 0
        b = 0
        for j in range(HW):
            if (i >> j) & 1:
                if j % W < W - 1 and (i >> (j + 1)) & 1:
                    a += 1
                if j < HW - W and (i >> (j + W)) & 1:
                    b += 1
        if a == A and b == B:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    H, W, A, B = map(int, input().split())
    HW = H * W
    ans = 0
    for i in range(2 ** HW):
        a = 0
        b = 0
        for j in range(HW):
            if (i >> j) & 1:
                a += 1
            else:
                b += 1
        if a == A and b == B:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    H, W, A, B = map(int, input().split())
    count = 0
    for i in range(2 ** (H * W)):
        s = bin(i)[2:].zfill(H * W)
        if s.count('1') == A:
            m = [[s[j * W + k] for k in range(W)] for j in range(H)]
            if m == list(map(list, zip(*m))):
                count += 1
    print(count)

=======
Suggestion 5

def main():
    H, W, A, B = map(int, input().split())
    print((H - B) * (W - A) * A * B)

=======
Suggestion 6

def main():
    h, w, a, b = map(int, input().split())
    print((h - b) * (w - a))

=======
Suggestion 7

def main():
    H, W, A, B = map(int, input().split())
    print((H - B) * (W - A) + A * B)

=======
Suggestion 8

def main():
    H, W, A, B = map(int, input().split())
    N = H * W

    # 初期化
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            if i + 1 <= N:
                dp[i + 1][j] += dp[i][j]
            if j + 1 <= N:
                dp[i][j + 1] += dp[i][j]

    # dp[i][j]: i個の2*1のタイルとj個の1*1のタイルを使ってN個のマスを埋め尽くす方法の数
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # dp[i][j]: i個の2*1のタイルとj個の1*1のタイルを使ってN個のマスを埋め尽くす方法の数
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # 1*1のタイルを使わない場合
    # dp[i][0] = dp[i-1][0]
    # 2*1のタイルを使わない場合
    # dp[0][j] = dp[0][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # 1*1のタイルを使わない場合
    # dp[i][0] = dp[i-1][0]
    # 2*1のタイルを使わない場合
    # dp[0][j] = dp[0][j-1]

    # N個のマスを埋め尽くす方法の数
    ans = 0
    for i in range(A + 1):
        j = N - 2

=======
Suggestion 9

def main():
    H, W, A, B = map(int, input().split())
    print(H * W - (2 * A + B))

=======
Suggestion 10

def main():
    H, W, A, B = map(int, input().split())
    print(A*B*2 + (H-A)*(W-B)*2 + (H-A)*(W-B))
