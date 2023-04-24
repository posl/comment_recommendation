Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T = [0] * N
    X = [0] * N
    A = [0] * N
    for i in range(N):
        T[i], X[i], A[i] = map(int, input().split())
    # print(T)
    # print(X)
    # print(A)

    # すぬけ君がいる穴のリストを作成
    holes = [[] for _ in range(5)]
    for i in range(N):
        holes[X[i]].append([T[i], A[i]])
    # print(holes)

    # すぬけ君がいる穴のリストをソート
    for i in range(5):
        holes[i].sort()
    # print(holes)

    # すぬけ君を捕まえるのにかかる時間を計算
    # 捕まえるのにかかる時間は無視できるので、
    # すぬけ君がいる穴のリストの長さの最大値を求める
    max_len = 0
    for i in range(5):
        if len(holes[i]) > max_len:
            max_len = len(holes[i])
    # print(max_len)

    # 捕まえるのにかかる時間の最大値を求める
    ans = 0
    for i in range(max_len):
        sum_A = 0
        for j in range(5):
            if i < len(holes[j]):
                sum_A += holes[j][i][1]
        if sum_A > ans:
            ans = sum_A
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)
    # すぬけ君が出現する時刻の降順にソート
    T, X, A = zip(*sorted(zip(T, X, A), reverse=True))
    # 捕まえたすぬけ君の大きさの合計
    ans = 0
    # 捕まえたすぬけ君の大きさの合計を更新するかどうか
    update = [False] * N
    # 捕まえたすぬけ君の大きさの合計を更新するかどうかを更新する
    for i in range(N):
        for j in range(i + 1, N):
            # 捕まえたすぬけ君の大きさの合計を更新するかどうかを更新する
            if T[i] - T[j] >= abs(X[i] - X[j]) and not update[j]:
                update[j] = True
    # 捕まえたすぬけ君の大きさの合計を更新する
    for i in range(N):
        if update[i]:
            ans += A[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    T = []
    X = []
    A = []
    for i in range(N):
        t, x, a = map(int, input().split())
        T.append(t)
        X.append(x)
        A.append(a)

    # dp[i][j] = i番目のすぬけ君を捕まえる時の最大値
    dp = [[0 for j in range(5)] for i in range(N+1)]
    for i in range(N):
        for j in range(5):
            if T[i] < i+1:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][X[i]] + A[i])
    print(max(dp[N]))

=======
Suggestion 4

def main():
    N = int(input())
    data = []
    for _ in range(N):
        T, X, A = map(int, input().split())
        data.append([T, X, A])
    ans = 0
    dp = [[0] * 5 for _ in range(N + 1)]
    for i in range(N):
        for j in range(5):
            if j != data[i][1]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            else:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + data[i][2])
            if abs(j - data[i][1]) <= data[i][0] - i:
                dp[i + 1][data[i][1]] = max(dp[i + 1][data[i][1]], dp[i][j])
        ans = max(ans, max(dp[i + 1]))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    X = [0] * 5
    for i in range(N):
        T, X, A = map(int, input().split())
        X[T] += A
    for i in range(1, 5):
        X[i] += X[i - 1]
    print(max(X))

=======
Suggestion 6

def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    A.sort()
    dp = [[0] * 5 for _ in range(N)]
    for i in range(N):
        for j in range(5):
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j == A[i][1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + A[i][2])
            elif j - 1 == A[i][1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + A[i][2])
            elif j + 1 == A[i][1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j+1] + A[i][2])
    print(max(dp[N-1]))

=======
Suggestion 7

def main():
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += S[i][2]
        for j in range(i+1, N):
            if S[i][0] == S[j][0] and S[i][1] == S[j][1]:
                ans -= S[j][2]
                break
    print(ans)

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    T_X_A = [list(map(int, input().split())) for _ in range(N)]
    #print(T_X_A)
    #print(N)
    #print(T_X_A[0])
    #print(T_X_A[0][0])
    #print(T_X_A[0][1])
    #print(T_X_A[0][2])
    #print(T_X_A[0][1] == T_X_A[1][1])
    #print(T_X_A[0][0] == T_X_A[1][0])
    #print(T_X_A[0][1] == T_X_A[1][1] and T_X_A[0][0] == T_X_A[1][0])

    #1つ目のすぬけ君の座標
    X1 = T_X_A[0][1]
    #1つ目のすぬけ君の大きさ
    A1 = T_X_A[0][2]
    #1つ目のすぬけ君の出現時刻
    T1 = T_X_A[0][0]
    #print(X1)
    #print(A1)
    #print(T1)

    #2つ目のすぬけ君の座標
    X2 = T_X_A[1][1]
    #2つ目のすぬけ君の大きさ
    A2 = T_X_A[1][2]
    #2つ目のすぬけ君の出現時刻
    T2 = T_X_A[1][0]
    #print(X2)
    #print(A2)
    #print(T2)

    #3つ目のすぬけ君の座標
    X3 = T_X_A[2][1]
    #3つ目のすぬけ君の大きさ
    A3 = T_X_A[2][2]
    #3つ目のすぬけ君の出現時刻
    T3 = T_X_A[2][0]
    #print(X3)
    #print(A3)
    #print(T3

=======
Suggestion 9

def main():
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    data.sort()
    #print(data)
    #print(N)
    #print(data)
    #print(data[0][0])
    #print(data[0][1])
    #print(data[0][2])
    #print(data[1][0])
    #print(data[1][1])
    #print(data[1][2])
    #print(data[2][0])
    #print(data[2][1])
    #print(data[2][2])
    #print(data[3][0])
    #print(data[3][1])
    #print(data[3][2])
    #print(data[4][0])
    #print(data[4][1])
    #print(data[4][2])
    #print(data[5][0])
    #print(data[5][1])
    #print(data[5][2])
    #print(data[6][0])
    #print(data[6][1])
    #print(data[6][2])
    #print(data[7][0])
    #print(data[7][1])
    #print(data[7][2])
    #print(data[8][0])
    #print(data[8][1])
    #print(data[8][2])
    #print(data[9][0])
    #print(data[9][1])
    #print(data[9][2])
    #print(data[10][0])
    #print(data[10][1])
    #print(data[10][2])
    #print(data[11][0])
    #print(data[11][1])
    #print(data[11][2])
    #print(data[12][0])
    #print(data[12][1])
    #print(data[12][2])
    #print(data[13][0])
    #print(data[13][1])
    #print(data[13][2])
    #print(data[14][0])
    #print(data[14][1])
    #print(data[14][2])
    #print(data[15][0])
    #print(data[15][1])
    #print(data[15][2])
    #print(data[16][0])
    #print(data[16][1])

=======
Suggestion 10

def main():
    N = int(input())
    T_X_A = [list(map(int, input().split())) for _ in range(N)]
    #print(T_X_A)
    #print(N)
    dp = [[0]*5 for _ in range(10**5+1)]
    for i in range(N):
        for j in range(5):
            if T_X_A[i][1] == j:
                dp[T_X_A[i][0]][j] = max(dp[T_X_A[i][0]][j], dp[T_X_A[i][0]-1][j] + T_X_A[i][2])
            else:
                dp[T_X_A[i][0]][j] = max(dp[T_X_A[i][0]][j], dp[T_X_A[i][0]-1][j])
            dp[T_X_A[i][0]][j] = max(dp[T_X_A[i][0]][j], dp[T_X_A[i][0]-1][T_X_A[i][1]])
    
    #print(dp)
    print(max(dp[N]))
