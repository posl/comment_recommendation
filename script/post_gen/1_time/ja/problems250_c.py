Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    a = [i for i in range(1, N+1)]
    for i in range(Q):
        x = int(input())
        a[x-1], a[x] = a[x], a[x-1]
    print(*a)

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    a = [i for i in range(1, N+1)]
    for i in range(Q):
        x = int(input())
        a[x-1], a[x] = a[x], a[x-1]
    for i in range(N):
        print(a[i], end=' ')

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(range(1, N+1))
    for _ in range(Q):
        x = int(input())
        A[x-1], A[x] = A[x], A[x-1]
    print(*A)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = [i for i in range(1, N+1)]
    for i in range(Q):
        x = int(input())
        A[x-1], A[x] = A[x], A[x-1]
    print(*A)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    balls = [i for i in range(1, N + 1)]
    for i in range(Q):
        x = int(input())
        balls[x - 1], balls[x] = balls[x], balls[x - 1]
    print(*balls)

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = [i for i in range(1, N+1)]
    for i in range(Q):
        x = int(input()) - 1
        A[x], A[x+1] = A[x+1], A[x]
    print(*A)

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    ball = list(range(1, N+1))
    for _ in range(Q):
        x = int(input())
        p = ball.index(x)
        if p == N-1:
            ball[p], ball[p-1] = ball[p-1], ball[p]
        else:
            ball[p], ball[p+1] = ball[p+1], ball[p]
    print(*ball)

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    # x_i が書かれているボールをその右隣のボールと入れ替える。ただし、整数 x_i が書かれているボールが元々右端にあった場合、代わりに左隣のボールと入れ替える。
    #操作後において左から i  (1 ≦ i ≦ N) 番目のボールに書かれている整数を a_i とします。 a_1,...,a_N を求めてください。
    #制約
    #2 ≦ N ≦ 2 × 10^5
    #1 ≦ Q ≦ 2 × 10^5
    #1 ≦ x_i ≦ N
    #入力は全て整数
    #入力
    #入力は以下の形式で標準入力から与えられる。
    #N Q
    #x_1
    #.
    #.
    #.
    #x_Q
    #出力
    #a_1,...,a_N を空白区切りで出力せよ。
    #入力例 1
    #5 5
    #1
    #2
    #3
    #4
    #5
    #出力例 1
    #1 2 3 5 4
    #操作は以下のように行われます。  
    #1 と書かれたボールを右隣のボールと入れ替える。ボールに書かれた整数は左から 2,1,3,4,5 となる。
    #2 と書かれたボールを右隣のボールと入れ替える。ボールに書かれた整数は左から 1,2,3,4,5 となる。
    #3 と書かれたボールを右隣

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    #ボールの初期位置
    ball = [i for i in range(1, N+1)]
    #ボールの最終位置
    result = [0 for i in range(N)]
    #ボールの最終位置を求める
    for i in range(Q):
        x = int(input())
        #ボールの位置を入れ替える
        ball[x-1], ball[x] = ball[x], ball[x-1]
    #ボールの最終位置を求める
    for i in range(N):
        result[ball[i]-1] = i+1
    #出力
    print(*result)

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    # 0 で初期化
    balls = [0] * N
    # 1 から N まで代入
    for i in range(N):
        balls[i] = i + 1
    # 操作
    for i in range(Q):
        x = int(input())
        # 交換
        balls[x - 1], balls[x] = balls[x], balls[x - 1]
    # 出力
    for i in range(N):
        print(balls[i], end = " ")
