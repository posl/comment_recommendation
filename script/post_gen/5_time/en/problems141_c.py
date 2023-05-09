Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [0] * N
    for a in A:
        score[a-1] += 1
    for i in range(N):
        if K + score[i] - Q > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

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
Suggestion 3

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [K-Q for _ in range(N)]
    for a in A:
        score[a-1] += 1
    for s in score:
        if s > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    players = [K-Q] * N
    for a in A:
        players[a-1] += 1
    for p in players:
        if p > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 5

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    p = [k-q] * n
    for i in a:
        p[i-1] += 1
    for i in p:
        if i > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    players = [k - q for _ in range(n)]
    for i in a:
        players[i-1] += 1
    for i in players:
        if i > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    players = [k - q for _ in range(n)]
    for i in a:
        players[i - 1] += 1
    for i in players:
        if i > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 8

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    X = [0] * N
    for a in A:
        X[a - 1] += 1
    for x in X:
        if K - Q + x > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def solve():
    n,k,q=map(int,input().split())
    a=[0]*n
    for i in range(q):
        a[int(input())-1]+=1
    for i in range(n):
        if q-a[i]>=k:
            print('No')
        else:
            print('Yes')
solve()
