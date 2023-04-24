Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    n,k,q = map(int,input().split())
    a = [0]*n
    for i in range(q):
        a[int(input())-1] += 1
    for i in range(n):
        if k - q + a[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    points = [K-Q for _ in range(N)]
    for a in A:
        points[a-1] += 1
    for p in points:
        if p > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [K for _ in range(N)]
    for i in range(Q):
        score[A[i]-1] += 1
    for i in range(N):
        if score[i] <= Q:
            print("No")
        else:
            print("Yes")

=======
Suggestion 5

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    scores = [K] * N
    for a in A:
        scores[a - 1] += 1
    for score in scores:
        if score - Q > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    cnt = [0] * n
    for i in range(q):
        cnt[a[i]-1] += 1
    for i in range(n):
        if k - q + cnt[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    n, k, q = map(int, input().split())
    a = []
    for i in range(q):
        a.append(int(input()))
    score = [k] * n
    for i in range(q):
        score[a[i] - 1] -= 1
    for i in range(n):
        if score[i] <= 0:
            print("No")
        else:
            print("Yes")

=======
Suggestion 8

def main():
    N,K,Q = map(int,input().split())
    A = [int(input()) for _ in range(Q)]
    ans = [K-Q for _ in range(N)]
    for a in A:
        ans[a-1] += 1
    for a in ans:
        if a > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def problem141c():
    n,k,q = map(int,input().split())
    a = [int(input()) for _ in range(q)]
    result = [0 for _ in range(n)]
    for i in range(q):
        result[a[i]-1] += 1
    for i in range(n):
        if k - q + result[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def judge(n,k,q,a):
    ans = [0]*n
    score = k
    for i in a:
        ans[i-1] += 1
    for j in ans:
        if score - q + j > 0:
            print("Yes")
        else:
            print("No")
