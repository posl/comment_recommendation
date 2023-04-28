Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [K - Q] * N
    for a in A:
        score[a - 1] += 1
    for s in score:
        if s > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    n,k,q = map(int,input().split())
    a = [k-q for i in range(n)]
    for i in range(q):
        a[int(input())-1] += 1
    for i in range(n):
        print("Yes" if a[i] > 0 else "No")

=======
Suggestion 3

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [K for _ in range(N)]
    for a in A:
        score[a-1] += 1
    for s in score:
        if s-Q > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [K - Q for _ in range(N)]
    for i in range(Q):
        score[A[i] - 1] += 1
    for i in score:
        if i <= 0:
            print('No')
        else:
            print('Yes')

=======
Suggestion 5

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    score = [K - Q] * N
    for a in A:
        score[a-1] += 1
    for s in score:
        if s > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    n, k, q = map(int, input().split())
    players = [k-q]*n
    for i in range(q):
        players[int(input())-1] += 1
    for i in range(n):
        if players[i] > 0:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    n, k, q = map(int, input().split())
    a = [int(input()) for _ in range(q)]
    p = [k-q for _ in range(n)]
    for i in a:
        p[i-1] += 1
    for i in p:
        if i <= 0:
            print("No")
        else:
            print("Yes")

main()

=======
Suggestion 8

def main():
    N,K,Q = map(int,input().split())
    A = [int(input()) for i in range(Q)]
    P = [K-Q]*N
    for i in range(Q):
        P[A[i]-1] += 1
    for i in range(N):
        if P[i] > 0:
            print("Yes")
        else:
            print("No")

main()

=======
Suggestion 9

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    A = [K - Q + 1 for _ in range(N)]
    for i in range(Q):
        A[A_i - 1] += 1
    for i in range(N):
        if A[i] > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]

    # N個の要素がKのリストを作成
    score_list = [K] * N

    for a in A:
        score_list[a-1] -= 1

    for score in score_list:
        if score > 0:
            print("Yes")
        else:
            print("No")
