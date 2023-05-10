Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    # print(N, K, P)
    for i in range(N):
        # print(i)
        if sum(P[i]) >= K:
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
        p[i].sort(reverse=True)
    for i in range(n):
        p[i] = sum(p[i][:k])
    for i in range(n):
        if p[i] >= sum(p[:k]):
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(sum(map(int, input().split())))
    P.sort(reverse=True)
    print('Yes' if P[K-1] > 0 else 'No')

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    score = [list(map(int, input().split())) for _ in range(N)]

    rank = [0] * N
    for i in range(N):
        rank[i] = score[i][0] + score[i][1] + score[i][2]

    for i in range(N):
        if rank[i] >= rank[K-1]:
            if rank[i] == rank[K-1]:
                if score[i][0] + score[i][1] + score[i][2] > score[K-1][0] + score[K-1][1] + score[K-1][2]:
                    print("Yes")
                else:
                    print("No")
            else:
                print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    N, K = map(int, input().split())

    for i in range(N):
        P = list(map(int, input().split()))
        if sum(P) >= K:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def solve():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    p.sort(key=lambda x: sum(x), reverse=True)
    for i in range(n):
        if i < k:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for i in range(N)]
    P_sum = []
    for i in range(N):
        P_sum.append(sum(P[i]))
    P_sum.sort(reverse=True)
    for i in range(N):
        if P_sum[i] >= P_sum[K-1]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    for _ in range(N):
        P = list(map(int, input().split()))
        if sum(P) >= 3 * K:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    for i in range(n):
        p[i].append(sum(p[i]))
    p.sort(key=lambda x: x[3], reverse=True)
    for i in range(n):
        if i < k:
            print('Yes')
        else:
            print('No')

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(n)]
    p_sum = [0] * n
    for i in range(n):
        p_sum[i] = sum(p[i])
    p_sum.sort(reverse=True)
    for i in range(n):
        if p_sum[i] > p_sum[k-1]:
            print("No")
        else:
            print("Yes")
