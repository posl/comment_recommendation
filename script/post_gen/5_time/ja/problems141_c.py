Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    scores = [K-Q] * N
    for a in A:
        scores[a-1] += 1
    for score in scores:
        if score > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    P = [K - Q] * N
    for a in A:
        P[a - 1] += 1
    for p in P:
        if p > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    #print(n, k, q)
    #print(a)
    score = [0] * n
    for i in range(q):
        score[a[i]-1] += 1
    
    for i in range(n):
        if k - q + score[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    n, k, q = map(int, input().split())
    ans = [0] * n
    for _ in range(q):
        a = int(input())
        ans[a-1] += 1
    for i in range(n):
        if k - q + ans[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    ans = [k - q] * n
    for i in a:
        ans[i-1] += 1
    for i in ans:
        if i > 0:
            print('Yes')
        else:
            print('No')

main()

=======
Suggestion 6

def main():
    n, k, q = map(int, input().split())
    score = [k] * n
    for _ in range(q):
        a = int(input())
        score[a-1] += 1
    for i in range(n):
        if score[i] > q:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    # データ入力
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]

    # 各参加者のポイント
    points = [K - Q] * N

    # 正解者のポイントを増やす
    for a in A:
        points[a-1] += 1

    # 各参加者のポイントが 0 以下なら敗退
    for point in points:
        if point <= 0:
            print('No')
        else:
            print('Yes')

=======
Suggestion 8

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    ans = [K-Q for _ in range(N)]
    for a in A:
        ans[a-1] += 1
    for i in range(N):
        if ans[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    ans = [0] * N
    for i in range(Q):
        ans[A[i] - 1] += 1
    for i in range(N):
        if K - Q + ans[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 10

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for i in range(q)]
    p = [0] * n

    for i in range(q):
        p[a[i]-1] += 1

    for i in range(n):
        if k - (q - p[i]) > 0:
            print('Yes')
        else:
            print('No')
