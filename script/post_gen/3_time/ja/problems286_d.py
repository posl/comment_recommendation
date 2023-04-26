Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    dp = [[False for i in range(X+1)] for j in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(X+1):
            for k in range(B[i]+1):
                if j >= A[i] * k and dp[i][j - A[i] * k]:
                    dp[i+1][j] = True

    if dp[N][X]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(N):
        for j in range(B[i]):
            X -= A[i]
            if X == 0:
                print("Yes")
                return
    print("No")

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(2**N):
        sum = 0
        for j in range(N):
            if (i>>j & 1):
                sum += A[j] * B[j]
        if (sum == X):
            print("Yes")
            return
    print("No")

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    for i in range(2 ** n):
        sum = 0
        for j in range(n):
            if (i >> j) & 1:
                sum += a[j] * b[j]
        if sum == x:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def main():
    #入力
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #解答
    for i in range(N):
        for j in range(B[i]+1):
            if A[i]*j == X:
                print("Yes")
                return
            elif A[i]*j > X:
                break
            else:
                X -= A[i]
    print("No")

=======
Suggestion 6

def main():
    N,X = map(int,input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i],B[i] = map(int,input().split())
    for i in range(N):
        if X >= A[i] * B[i]:
            X -= A[i] * B[i]
        else:
            X %= A[i]
    if X == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N, X = map(int,input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int,input().split())
    
    for i in range(N):
        for j in range(B[i]+1):
            if X == A[i] * j:
                print('Yes')
                return
    
    print('No')
    return

=======
Suggestion 8

def main():
    # 入力
    N, X = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # 1枚も使わない場合を追加
    A.append(0)
    B.append(0)

    # 計算
    ans = "No"
    for i in range(N+1):
        for j in range(N+1):
            if A[i]*i + A[j]*j == X:
                ans = "Yes"

    # 出力
    print(ans)

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    a, b = [], []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    print("Yes" if solve(n, x, a, b) else "No")

=======
Suggestion 10

def main():
    # input
    N, X = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(N)]

    # compute
    for i in range(N):
        if ABs[i][0]*ABs[i][1] >= X:
            ABs[i][1] = X//ABs[i][0]
            X -= ABs[i][0]*ABs[i][1]
        else:
            X -= ABs[i][0]*ABs[i][1]

    # output
    if X == 0:
        print('Yes')
    else:
        print('No')
