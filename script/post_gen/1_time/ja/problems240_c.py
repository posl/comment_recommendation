Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [False] * (X + 1)
    dp[0] = True
    for i in range(N):
        for j in range(X - b[i], -1, -1):
            if dp[j]:
                dp[j + b[i]] = True
                dp[j + a[i]] = True
    if dp[X]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    dp = [False] * (X + 1)
    dp[0] = True
    for i in range(N):
        for j in range(X + 1):
            if dp[j]:
                if j + a[i] <= X:
                    dp[j + a[i]] = True
                if j + b[i] <= X:
                    dp[j + b[i]] = True
    if dp[X]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    a = [0] * N
    b = [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    #print(N, X)
    #print(a)
    #print(b)
    for i in range(N):
        if X >= a[i] and X <= b[i]:
            print("Yes")
            exit()
        else:
            X = X - a[i]
            if X < 0:
                print("No")
                exit()

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    dp = [False] * (X + 1)
    dp[0] = True
    for i in range(N):
        for j in range(X + 1):
            if dp[j] and j + A[i] <= X:
                dp[j + A[i]] = True
            if dp[j] and j + B[i] <= X:
                dp[j + B[i]] = True
    if dp[X]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b

    dp = [False] * (X + 1)
    dp[0] = True
    for i in range(N):
        for j in range(X + 1):
            if dp[j]:
                if j + A[i] <= X:
                    dp[j + A[i]] = True
                if j + B[i] <= X:
                    dp[j + B[i]] = True

    if dp[X]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    # 入力
    N, X = map(int, input().split())
    a, b = [0] * N, [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    # x座標の初期値
    x = 0
    # N回のジャンプ
    for i in range(N):
        # a_iかb_iのどちらかを選択
        if abs(X - (x + a[i])) <= abs(X - (x + b[i])):
            x = x + a[i]
        else:
            x = x + b[i]
    # 出力
    if x == X:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        A.append(b)
    if X in A:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    #N, X = 4, 12
    #a = [[1, 8], [5, 7], [3, 4], [2, 6]]
    a = []
    for i in range(N):
        a.append(list(map(int, input().split())))
    #print(a)
    #print(a[0][0])
    #print(a[0][1])
    #print(a[1][0])
    #print(a[1][1])
    #print(a[2][0])
    #print(a[2][1])
    #print(a[3][0])
    #print(a[3][1])
    #print(a[0][0] + a[0][1])
    #print(a[1][0] + a[1][1])
    #print(a[2][0] + a[2][1])
    #print(a[3][0] + a[3][1])
    #print(a[0][0] + a[1][0] + a[2][0] + a[3][0])
    #print(a[0][1] + a[1][1] + a[2][1] + a[3][1])
    #print(a[0][0] + a[1][0] + a[2][0] + a[3][0] + a[0][1] + a[1][1] + a[2][1] + a[3][1])
    #print(a[0][0] + a[1][0] + a[2][0] + a[3][0] + a[0][1] + a[1][1] + a[2][1] + a[3][1] + X)
    #print(a[0][0] + a[1][0] + a[2][0] + a[3][0] + a[0][1] + a[1][1] + a[2][1] + a[3][1] + X == 12)
    #print(a[0][0] + a[1][0] + a[2][0] + a[3][0] + a[0][1] + a[

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    AB.sort(key=lambda x: x[1])
    for a, b in AB:
        if X < a:
            print("No")
            return
        X -= a
    if X == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    #入力
    N, X = map(int, input().split())
    ab = []
    for i in range(N):
        ab.append(list(map(int, input().split())))
    #print(N, X, ab)

    #処理
    ans = "No"
    for i in range(2**N):
        #print(i)
        bi = bin(i)[2:].zfill(N)
        #print(bi)
        sum = 0
        for j in range(N):
            if bi[j] == "0":
                sum += ab[j][0]
            else:
                sum += ab[j][1]
        if sum == X:
            ans = "Yes"
            break

    #出力
    print(ans)
