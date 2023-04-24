Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n, x, y = map(int, input().split())
    if n == 1:
        print(0)
        return
    if n == 2:
        print(x)
        return
    if n == 3:
        print(x + y)
        return
    a = [0] * (n + 1)
    a[1] = 0
    a[2] = x
    a[3] = x + y
    for i in range(4, n + 1):
        a[i] = min(a[i - 1] + x, a[i - 2] + y)
    print(a[n])

=======
Suggestion 2

def main():
    N, X, Y = map(int, input().split())
    ans = 0
    for i in range(1, N):
        ans += i * (N - i)
    ans *= X
    ans += N * Y
    print(ans)

=======
Suggestion 3

def main():
    #入力
    N, X, Y = map(int, input().split())
    #初期化
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][1] = 1
    #漸化式
    for i in range(N):
        for j in range(N + 1):
            #赤い宝石を青い宝石に変換
            if j > 1:
                dp[i + 1][j - 1] += dp[i][j] * (j - 1)
            #青い宝石を赤い宝石に変換
            if j < N:
                dp[i + 1][j + 1] += dp[i][j] * (N - j)
            #青い宝石を赤い宝石に変換
            if j < N - 1:
                dp[i + 1][j + 2] += dp[i][j] * (N - j) * Y
            #赤い宝石を青い宝石に変換
            if j > 0:
                dp[i + 1][j] += dp[i][j] * j * X
    #出力
    print(dp[N][1])

=======
Suggestion 4

def main():
    N, X, Y = map(int, input().split())
    print(0)

=======
Suggestion 5

def main():
    N,X,Y = map(int,input().split())
    #print(N)
    #print(X)
    #print(Y)
    #pr

=======
Suggestion 6

def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)
    #print("N={}, X={}, Y={}".format(N, X, Y))
    #print("N="+str(N)+", X="+str(X)+", Y="+str(Y))

    #print("N={}, X={}, Y={}".format(N, X, Y))
    #print("N="+str(N)+", X="+str(X)+", Y="+str(Y))

    #print("N={}, X={}, Y={}".format(N, X, Y))
    #print("N="+str(N)+", X="+str(X)+", Y="+str(Y))

    #print("N={}, X={}, Y={}".format(N, X, Y))
    #print("N="+str(N)+", X="+str(X)+", Y="+str(Y))

    #print("N={}, X={}, Y={}".format(N, X, Y))
    #print("N="+str(N)+", X="+str(X)+", Y="+str(Y))

    #print("N={}, X={}, Y={}".format(N, X, Y))
    #print("N="+str(N)+", X="+str(X)+", Y="+str(Y))

    #print("N={}, X={}, Y={}".format(N, X, Y))
    #print("N="+str(N)+", X="+str(X)+", Y="+str(Y))

    #print("N={}, X={}, Y={}".format(N, X, Y))
    #print("N="+str(N)+", X="+str(X)+", Y="+str(Y))

    #print("N={}, X={}, Y={}".format(N, X, Y))
    #print("N="+str(N)+", X="+str(X)+", Y="+str(Y))

    #print("N={}, X={}, Y={}".format(N, X, Y))
    #print("N="+str(N)+", X="+str(X)+", Y="+str(Y))

    #print("N={}, X={}, Y={}".format(N, X, Y))
    #print("N="+str(N)+", X="+str(X)+", Y="+str(Y))

    #print("N={}, X={}, Y={}".format(N, X, Y))
    #print("N="+str(N)+", X="+str(X)+", Y="+str(Y))

    #print("N={}, X

=======
Suggestion 7

def main():
    N, X, Y = map(int, input().split())
    # レベル 1 の青い宝石の個数を求める
    def get_blue(N):
        if N == 1:
            return 0
        elif N == 2:
            return X
        else:
            return Y * get_blue(N - 1) + get_blue(N - 2)
    # レベル 1 の青い宝石の個数を出力
    print(get_blue(N))

=======
Suggestion 8

def main():
    N, X, Y = map(int,input().split())
    print(N*X*Y)

=======
Suggestion 9

def main():
    N, X, Y = map(int, input().split())
    #print(N, X, Y)

    # 1からNまでの宝石の数をリストに格納する
    # 1からNまでの宝石の数をリストに格納する
    gem = [0] * (N + 1)
    gem[1] = 1
    #print(gem)

    # 1からNまでの宝石の数をリストに格納する
    for i in range(1, N):
        gem[i + 1] = gem[i] * X + gem[i - 1] * Y
    #print(gem)

    # 答えを出力する
    print(gem[N])
