Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
    ans += min([AB[i][1] for i in range(N)])
    ans *= X
    print(ans)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for i in range(N):
        ans += AB[i][0] + AB[i][1]
        if ans > X:
            print(i+1)
            return
    print(N)
main()

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])

    time = 0
    for a, b in AB:
        time += a + b
        if time > X:
            break
    else:
        print(time)
        return

    print(time - (time - X) // 2)

=======
Suggestion 4

def solve():
    n, x = map(int, input().split())
    a_b = [tuple(map(int, input().split())) for _ in range(n)]
    a_b.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for a, b in a_b:
        ans += a + b
        if ans > x:
            print(ans - a - b)
            return
    print(ans)

solve()

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    # print(AB)
    ans = 0
    for i, (a, b) in enumerate(AB):
        if X > 0:
            ans += a + b
            X -= 1
        else:
            ans += b
    print(ans)

=======
Suggestion 6

def main():
    # input
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    # solve
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        ans = max(ans, AB[i][0] + AB[i][1] * (X - 1))
    # output
    print(ans)

=======
Suggestion 7

def solve():
    N,X = map(int,input().split())
    AB = []
    for _ in range(N):
        AB.append(list(map(int,input().split())))
    AB.sort()
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
        if ans > X:
            print(ans)
            return
    print(ans)
    return

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]

    # dp[i][j] = i番目のステージをj回クリアするのにかかる最小時間
    dp = [[float("inf")] * (X + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for j in range(X + 1):
            # i番目のステージをj回クリアするのにかかる最小時間
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + AB[i][0] + AB[i][1] * j)
            # i番目のステージをj回クリアするのにかかる最小時間
            if j > 0:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i + 1][j - 1] + AB[i][1])
    print(dp[-1][-1])

=======
Suggestion 9

def solve():
    N,X = map(int, input().split())
    AB = []
    for _ in range(N):
        AB.append(list(map(int, input().split())))
    #print(N,X,AB)
    #N,X,AB = 3,4,[[3,4],[2,3],[4,2]]
    #N,X,AB = 10,1000000000,[[3,3],[1,6],[4,7],[1,8],[5,7],[9,9],[2,4],[6,4],[5,1],[3,1]]
    #N,X,AB = 2,1000000000,[[1000000000,1000000000],[1000000000,1000000000]]
    #N,X,AB = 2,1000000000,[[1,1],[1,1]]
    #N,X,AB = 2,1000000000,[[1,1],[1,1000000000]]
    #N,X,AB = 2,1000000000,[[1,1000000000],[1,1]]
    #N,X,AB = 2,1000000000,[[1,1000000000],[1000000000,1]]
    #N,X,AB = 2,1000000000,[[1000000000,1],[1,1000000000]]
    #N,X,AB = 2,1000000000,[[1000000000,1],[1000000000,1]]
    #N,X,AB = 2,1000000000,[[1000000000,1000000000],[1,1]]
    #N,X,AB = 2,1000000000,[[1000000000,1000000000],[1,1000000000]]
    #N,X,AB = 2,1000000000,[[1000000000,1000000000],[1000000000,1]]
    #N,X,AB = 2,1000000000,[[1000000000,1000000000],[1000000000,1000000000]]
    #N,X,AB = 2,1000000000,[[1,1],[1,1]]
    #N,X,AB = 2,1000000000,[[

=======
Suggestion 10

def main():
    # input
    N, X = map(int, input().split())
    # A[i], B[i]
    AB = [list(map(int, input().split())) for _ in range(N)]

    # solve
    # 1. sort by A[i] + B[i]
    # 2. select minimum X stages
    AB.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for ab in AB[:X]:
        ans += ab[0] + ab[1]
    # 3. add remain stages
    for ab in AB[X:]:
        ans += ab[0]

    # output
    print(ans)
