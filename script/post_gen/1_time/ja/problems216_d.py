Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    k = [0] * m
    a = [0] * m
    for i in range(m):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))
    ball = [0] * (n + 1)
    for i in range(m):
        for j in range(k[i]):
            ball[a[i][j]] += 1
    for i in range(n + 1):
        if ball[i] % 2 != 0:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(M):
        k = int(input())
        a = list(map(int, input().split()))
        A.append(a)
    #print(N, M, A)
    B = [0] * N
    for a in A:
        for x in a:
            B[x - 1] += 1
    for b in B:
        if b % 2 != 0:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(M):
        k = int(input())
        A.append(list(map(int, input().split())))
    print('Yes' if solve(N, M, A) else 'No')

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [0] * (N + 1)
    for _ in range(M):
        _, *a = map(int, input().split())
        for x in a:
            A[x] += 1
    print('Yes' if all(x % 2 == 0 for x in A) else 'No')

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [0] * M
    for i in range(M):
        k = int(input())
        A[i] = [int(x) for x in input().split()]
    cnt = [0] * (N + 1)
    for i in range(M):
        for j in range(k):
            cnt[A[i][j]] += 1
    for i in range(1, N + 1):
        if cnt[i] % 2 == 1:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    balls = [0] * (N + 1)
    for _ in range(M):
        _, *a = map(int, input().split())
        for i in a:
            balls[i] += 1
    print("Yes" if all(i % 2 == 0 for i in balls) else "No")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(M):
        k = int(input())
        A.append(list(map(int, input().split())))
    cnt = [0] * N
    for i in range(M):
        for j in range(k):
            cnt[A[i][j]-1] += 1
    for i in range(N):
        if cnt[i] % 2 == 1:
            print('No')
            return
    print('Yes')

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = [0] * N
    for i in range(M):
        input()
        for x in map(int, input().split()):
            A[x - 1] += 1
    print('Yes' if all(x % 2 == 0 for x in A) else 'No')

=======
Suggestion 9

def solve():
    import sys
    readline = sys.stdin.readline
    N, M = map(int, readline().split())
    A = [0] * (N+1)
    for _ in range(M):
        K = int(readline())
        for a in map(int, readline().split()):
            A[a] += 1
    for a in A:
        if a % 2 != 0:
            print('No')
            return
    print('Yes')
    return

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    #print(N, M)
    #print(A)

    # ボールの色をキーにして、ボールの個数を値とする辞書
    ball = {}
    for i in range(M):
        for j in range(1, A[i][0]+1):
            if A[i][j] in ball:
                ball[A[i][j]] += 1
            else:
                ball[A[i][j]] = 1

    #print(ball)
    # ボールの個数が奇数個であるとき、目標を達成することができない
    for b in ball:
        if ball[b] % 2 == 1:
            print('No')
            return

    print('Yes')
