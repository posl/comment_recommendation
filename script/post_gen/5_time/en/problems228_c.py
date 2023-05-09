Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    for i in range(N):
        P[i].append(sum(P[i]))
    P.sort(key=lambda x:x[3], reverse=True)
    for i in range(N):
        if i < K:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    for i in range(n):
        p[i].append(sum(p[i]))
    p.sort(key=lambda x: x[3], reverse=True)
    print('Yes') if k <= p.index(p[k-1])+1 else print('No')

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        P[i].append(sum(P[i]))
    P = sorted(P, key=lambda x: x[3], reverse=True)
    for i in range(N):
        if P[i][3] == P[K-1][3]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    p_list = []
    for i in range(n):
        p_list.append(list(map(int, input().split())))
    for i in range(n):
        if sum(p_list[i]) < k * 3:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    for pi in p:
        if sum(pi) < k*3:
            print("No")
        else:
            print("Yes")

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    scores = []
    for i in range(N):
        scores.append(list(map(int, input().split())))
    for i in range(N):
        if scores[i][0] + scores[i][1] + scores[i][2] >= 300 * 3 - K:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    for i in range(N):
        if sum(P[i]) < K*3:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def problems228_c():
    n,k = map(int, input().split())
    p = [list(map(int, input().split())) for i in range(n)]
    for i in range(n):
        p[i].append(sum(p[i]))
    p.sort(key=lambda x: x[3], reverse=True)
    for i in range(n):
        if i < k:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    print('Yes' if sum([sum(p) >= K for p in P]) == N else 'No')

=======
Suggestion 10

def problems228_c():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    print('Yes' if k <= sum(sorted([sum(p[i]) for i in range(n)], reverse=True)[:k]) else 'No')
