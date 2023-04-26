Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    a = [i for i in range(1, N + 1)]
    for i in range(Q):
        x = int(input())
        a[x - 1], a[x] = a[x], a[x - 1]
    for i in range(N):
        print(a[i], end=" ")
    print()

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    balls = [i for i in range(1, N+1)]
    for _ in range(Q):
        x = int(input())
        balls[x-1], balls[x] = balls[x], balls[x-1]
    print(*balls)

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    balls = list(range(N+1))
    for i in range(Q):
        x = int(input())
        balls[x], balls[x+1] = balls[x+1], balls[x]
    print(*balls[1:])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    ball = [i for i in range(1,N+1)]
    for i in range(Q):
        x = int(input())
        ball[x-1], ball[x] = ball[x], ball[x-1]
    print(*ball)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    ball = [i for i in range(1, N+1)]
    for q in range(Q):
        x = int(input())
        ball[x-1], ball[x] = ball[x], ball[x-1]
    print(*ball)

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    balls = [i for i in range(1, N+1)]
    for i in range(Q):
        x = int(input())
        if x == 1:
            balls[0], balls[1] = balls[1], balls[0]
        elif x == N:
            balls[N-2], balls[N-1] = balls[N-1], balls[N-2]
        else:
            balls[x-2], balls[x-1] = balls[x-1], balls[x-2]
    print(*balls)

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    ball = [i for i in range(1, N+1)]
    for i in range(Q):
        x = int(input())
        if x == N:
            ball[x-1], ball[0] = ball[0], ball[x-1]
        else:
            ball[x-1], ball[x] = ball[x], ball[x-1]
    print(*ball)

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    A = [i for i in range(1, N + 1)]
    for _ in range(Q):
        x = int(input())
        if x == N:
            A[0], A[N - 1] = A[N - 1], A[0]
        else:
            A[x], A[x - 1] = A[x - 1], A[x]
    print(*A)

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    x = [int(input()) for _ in range(Q)]
    a = [i for i in range(1, N+1)]
    for i in x:
        a[i-1], a[i] = a[i], a[i-1]
    print(*a)

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    a = [i for i in range(1, N+1)]
    for _ in range(Q):
        x = int(input())
        a_index = a.index(x)
        if a_index == N-1:
            a[a_index], a[a_index-1] = a[a_index-1], a[a_index]
        else:
            a[a_index], a[a_index+1] = a[a_index+1], a[a_index]
    print(*a)
