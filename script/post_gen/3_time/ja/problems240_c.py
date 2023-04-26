Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(N):
        X -= a[i]
        if X <= 0:
            print("Yes")
            return
        X -= b[i]
        if X <= 0:
            print("Yes")
            return
    print("No")
    return

main()

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(N, X)
    #print(a)
    #print(b)

    #座標0から座標Xまでの距離
    distance = X
    #print(distance)
    #座標0から座標Xまでの距離を超えるまでのジャンプ回数を求める
    for i in range(N):
        if distance <= a[i]:
            distance = distance - a[i]
        elif distance <= b[i]:
            distance = distance - b[i]
        #print(distance)
    #print(distance)
    if distance > 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #print(N, X)
    #print(A)
    #print(B)
    for i in range(N):
        X -= A[i]
        if X <= 0:
            print('Yes')
            return
        X -= B[i]
        if X <= 0:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        A, B = map(int, input().split())
        a.append(A)
        b.append(B)
    #print(a)
    #print(b)
    dp = [0] * (X + 1)
    dp[0] = 1
    for i in range(1, X + 1):
        for j in range(N):
            if i - a[j] >= 0 and dp[i - a[j]] == 1:
                dp[i] = 1
            elif i - b[j] >= 0 and dp[i - b[j]] == 1:
                dp[i] = 1
    #print(dp)
    print("Yes" if dp[X] == 1 else "No")

=======
Suggestion 5

def main():
    #入力
    N, X = map(int, input().split())
    a = []
    b = []
    for i in range(N):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)

    #処理
    for i in range(N):
        if X <= a[i]:
            X = X - a[i]
        else:
            X = X - b[i]

    #出力
    if X == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    alist = []
    blist = []
    for i in range(N):
        a, b = map(int, input().split())
        alist.append(a)
        blist.append(b)
    for i in range(N):
        if X - alist[i] >= 0:
            X -= alist[i]
        elif X - blist[i] >= 0:
            X -= blist[i]
        else:
            print("No")
            return
    print("Yes")

=======
Suggestion 7

def main():
    #入力
    N,X = map(int,input().split())
    a = []
    b = []
    for i in range(N):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(N,X,a,b)

    #処理
    #print(sum(a))
    if sum(a) > X:
        print("No")
        exit()
    if sum(b) < X:
        print("No")
        exit()
    else:
        print("Yes")
        exit()

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    for i in range(N):
        a, b = map(int, input().split())
        if a <= X <= b:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    sum = 0
    for i in range(N):
        a, b = map(int, input().split())
        sum += a
        if X < sum:
            print('No')
            exit()
        sum += b
        if X < sum:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N)]
    for (a, b) in ab:
        if X >= a and X <= b:
            print("Yes")
            exit()
    print("No")
