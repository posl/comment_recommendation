Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        p[i].sort(reverse=True)
    for i in range(n):
        if p[i][0] + p[i][1] + p[i][2] >= k:
            print('Yes')
        else:
            print('No')

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    p = [list(map(int,input().split())) for _ in range(n)]
    p.sort(key=lambda x:sum(x),reverse=True)
    p4 = [p[i][0] for i in range(n)]
    p4.sort(reverse=True)
    for i in range(n):
        if p4.index(p[i][0])+1<=k:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    n,k = map(int, input().split())
    n_list = []
    for i in range(n):
        n_list.append(list(map(int, input().split())))
    print(n_list)
    print(n,k)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    score = []
    for i in range(n):
        score.append(list(map(int, input().split())))
    for i in range(n):
        score[i].sort(reverse=True)
    for i in range(n):
        if score[i][0] + score[i][1] + score[i][2] >= k:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: sum(x), reverse=True)
    print("Yes" if P[K-1] == P[K] else "No")

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    p = sorted(p, key=lambda x: sum(x), reverse=True)
    for i in range(n):
        if i < k:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for i in range(n)]
    print(p)
    for i in range(n):
        p[i].append(sum(p[i]))
    print(p)
    p.sort(key=lambda x: x[3], reverse=True)
    print(p)
    for i in range(n):
        if p[i][3] > p[k-1][3]:
            print('No')
        else:
            print('Yes')

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    scores = []
    for i in range(n):
        scores.append(list(map(int, input().split())))
    print(scores)
    for i in range(n):
        scores[i].sort(reverse=True)
        if scores[i][0] + scores[i][1] + scores[i][2] >= k:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    P.sort(key=lambda x: sum(x), reverse=True)
    for i in range(N):
        if sum(P[i]) > sum(P[K - 1]):
            print('Yes')
        else:
            print('No')

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(list(map(int, input().split())))
    P.sort(key=lambda x: sum(x), reverse=True)
    for i in range(N):
        if i < K:
            print('Yes')
        else:
            print('No')
    return 0
