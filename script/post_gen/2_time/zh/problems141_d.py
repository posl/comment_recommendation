Synthesizing 10/10 solutions

=======
Suggestion 1

def survive(N, K, Q, A):
    score = [K] * N
    for i in range(Q):
        score[A[i]-1] -= 1
    for i in range(N):
        if score[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    N, K, Q = map(int, input().split())
    score = [K] * N
    for _ in range(Q):
        ans = int(input())
        score[ans - 1] += 1
    for i in range(N):
        if score[i] - Q <= 0:
            print("No")
        else:
            print("Yes")

=======
Suggestion 3

def main():
    n,k,q = map(int, input().split())
    players = [k] * n
    for _ in range(q):
        players[int(input())-1] -= 1
    for p in players:
        if p > 0:
            print("Yes")
        else:
            print("No")

main()

=======
Suggestion 4

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    ans = [0] * n
    for i in range(q):
        ans[a[i] - 1] += 1
    for i in range(n):
        if k - q + ans[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    n,k,q = map(int,input().split())
    scores = [k]*n
    for i in range(q):
        scores[int(input())-1] += 1
    for i in range(n):
        if scores[i] <= q:
            print("No")
        else:
            print("Yes")
    return 0

=======
Suggestion 6

def main():
    n,k,q = map(int,input().split())
    a = []
    for i in range(q):
        a.append(int(input()))
    #print(n,k,q,a)
    b = [k for i in range(n)]
    for i in range(q):
        b[a[i]-1] -= 1
    #print(b)
    for i in range(n):
        if b[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    pass

=======
Suggestion 8

def solve():
    n, k, q = map(int, input().split())
    score = [k for _ in range(n)]
    for _ in range(q):
        a = int(input())
        score[a - 1] += 1
    for i in range(n):
        if score[i] <= q:
            print("No")
        else:
            print("Yes")

=======
Suggestion 9

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [K-Q for _ in range(N)]
    for i in range(Q):
        score[A[i]-1] += 1
    for i in range(N):
        if score[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    n,k,q = map(int,input().split())
    a = [int(input()) for i in range(q)]
    score = [k]*n
    for i in range(q):
        score[a[i]-1] = score[a[i]-1] - 1
    for i in range(n):
        if score[i] > 0:
            print('Yes')
        else:
            print('No')
