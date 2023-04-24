Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, Q = map(int, input().split())
    point = [K] * N
    for _ in range(Q):
        A = int(input())
        point[A-1] += 1
    for i in range(N):
        point[i] -= Q
        if point[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    N, K, Q = map(int, input().split())
    point = [K] * N
    for _ in range(Q):
        point[int(input()) - 1] += 1
    for p in point:
        print("Yes" if p > Q else "No")

=======
Suggestion 3

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    points = [K - Q] * N
    for i in range(Q):
        points[A[i] - 1] += 1
    for i in range(N):
        if points[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    B = [K - Q] * N
    for i in range(Q):
        B[A[i] - 1] += 1
    for i in range(N):
        print("Yes" if B[i] > 0 else "No")

=======
Suggestion 5

def main():
    N, K, Q = map(int, input().split())
    scores = [K for _ in range(N)]
    for _ in range(Q):
        scores[int(input()) - 1] += 1
    for score in scores:
        print("Yes" if score > Q else "No")

=======
Suggestion 6

def main():
    N, K, Q = map(int, input().split())
    #N, K, Q = 10, 13, 15
    #A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
    A = [int(input()) for _ in range(Q)]
    #print(N, K, Q)
    #print(A)
    point = [K - Q] * N
    #print(point)
    for i in range(Q):
        point[A[i] - 1] += 1
    #print(point)
    for i in range(N):
        if point[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    N, K, Q = [int(x) for x in input().split()]
    A = [int(input()) for i in range(Q)]
    P = [K for i in range(N)]
    for i in range(Q):
        P[A[i]-1] += 1
    for i in range(N):
        if P[i] - Q > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    N,K,Q = map(int,input().split())
    A = [int(input()) for _ in range(Q)]
    ans = [K-Q]*N
    for a in A:
        ans[a-1] += 1
    for a in ans:
        if a > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]

    # 参加者のポイント
    point = [K - Q] * N

    # 正解した参加者のポイントを1増やす
    for a in A:
        point[a - 1] += 1

    # ポイントが0以下の参加者は敗退
    for p in point:
        if p > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]
    #print(N, K, Q)
    #print(A)
    #print([K - Q + A.count(i) for i in range(1, N+1)])
    print(*["Yes" if K - Q + A.count(i) > 0 else "No" for i in range(1, N+1)], sep='

')
