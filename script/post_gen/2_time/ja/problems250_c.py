Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = [i for i in range(1, n+1)]
    for i in range(q):
        x = int(input())
        a[x-1], a[x] = a[x], a[x-1]
    print(' '.join(map(str, a)))

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    a = list(range(1, N + 1))
    for i in range(Q):
        x = int(input())
        a[x - 1], a[x] = a[x], a[x - 1]
    print(*a)

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    a = [i for i in range(1, n+1)]
    for _ in range(q):
        x = int(input())
        a[x-1], a[x] = a[x], a[x-1]
    print(*a)

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = i + 1
    for i in range(q):
        x = int(input())
        for j in range(n):
            if a[j] == x:
                if j != n - 1:
                    a[j], a[j + 1] = a[j + 1], a[j]
                else:
                    a[j], a[j - 1] = a[j - 1], a[j]
                break
    for i in range(n):
        print(a[i], end = " ")

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    ball = [i for i in range(1, N+1)]
    for i in range(Q):
        x = int(input())
        ball[x-1], ball[x] = ball[x], ball[x-1]
    print(*ball)

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    ball = [0] * n
    for i in range(n):
        ball[i] = i + 1
    for i in range(q):
        x = int(input())
        for j in range(n):
            if ball[j] == x:
                ball[j], ball[j + 1] = ball[j + 1], ball[j]
                break
    for i in range(n):
        print(ball[i], end=" ")

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    a = list(range(1, N + 1))
    for i in range(Q):
        x = int(input())
        idx = a.index(x)
        if idx == len(a) - 1:
            a[idx], a[idx - 1] = a[idx - 1], a[idx]
        else:
            a[idx], a[idx + 1] = a[idx + 1], a[idx]
    print(*a)

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    a = [i + 1 for i in range(N)]
    b = [0] * N
    for _ in range(Q):
        x = int(input())
        b[x - 1] += 1
    for i in range(N):
        a[i] = a[i] - b[i]
    for i in range(N):
        a[i] = a[i] + b[a[i] - 1]
    print(*a)

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    # 1-indexed
    balls = [i for i in range(1, n+1)]
    for _ in range(q):
        x = int(input())
        # x-1番目のボールを右隣のボールと入れ替える
        # x-1番目のボールが右端にある場合は左隣のボールと入れ替える
        if x == n:
            balls[x-1], balls[x-2] = balls[x-2], balls[x-1]
        else:
            balls[x-1], balls[x] = balls[x], balls[x-1]
    print(*balls)

=======
Suggestion 10

def main():
    n, q = map(int, input().split())
    # ボールを並べる
    balls = [i for i in range(1, n + 1)]
    # ボールの位置を記録する
    ball_pos = [i for i in range(n)]
    for _ in range(q):
        x = int(input())
        # ボールを入れ替える
        # ボールの位置を記録する
        balls[ball_pos[x - 1]], balls[ball_pos[x - 1] + 1] = balls[ball_pos[x - 1] + 1], balls[ball_pos[x - 1]]
        ball_pos[x - 1], ball_pos[x - 1] + 1 = ball_pos[x - 1] + 1, ball_pos[x - 1]
        # ボールの位置を記録する
        if ball_pos[x - 1] == n - 1:
            ball_pos[x - 1] = 0
        else:
            ball_pos[x - 1] += 1
    print(*balls)
