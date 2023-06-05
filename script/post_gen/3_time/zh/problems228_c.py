Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    scores = []
    for _ in range(n):
        scores.append(sum(map(int, input().split())))
    print('\n'.join(['Yes' if s < scores[k-1] else 'No' for s in scores]))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    p.sort(key=lambda x: sum(x), reverse=True)
    for i in range(n):
        p[i].append(i + 1)
    p.sort(key=lambda x: x[3])
    for i in range(n):
        if p[i][3] <= k:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    scores.sort(key=lambda x: sum(x), reverse=True)
    scores = scores[:K]
    scores.sort(key=lambda x: x[0], reverse=True)
    scores = scores[:K]
    scores.sort(key=lambda x: x[1], reverse=True)
    scores = scores[:K]
    scores.sort(key=lambda x: x[2], reverse=True)
    scores = scores[:K]
    for i in range(N):
        if scores.count(scores[i]) > 0:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    P = []
    for i in range(N):
        P.append(tuple(map(int, input().split())))
    P.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    for i in range(K):
        if P[i][0] + P[i][1] + P[i][2] < P[K - 1][0] + P[K - 1][1] + P[K - 1][2]:
            print('No')
            return
    print('Yes')

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    p = []
    for i in range(n):
        p.append(list(map(int,input().split())))
    for i in range(n):
        p[i].sort()
    for i in range(n):
        if p[i][0] + p[i][1] + p[i][2] + 1 >= k:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    n,k = map(int, input().split())
    scores = []
    for i in range(n):
        scores.append(list(map(int, input().split())))
    scores.sort(key=lambda x: sum(x), reverse=True)
    scores = scores[:k]
    scores = [sum(x) for x in scores]
    scores.sort(reverse=True)
    for i in range(n):
        if sum(scores[i:]) < scores[k-1]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    a.sort(key=lambda x: sum(x), reverse=True)
    a = a[:k]

    for i in range(n):
        for j in range(3):
            if a[0][j] < a[i][j]:
                print('No')
                break
        else:
            print('Yes')

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(n)]
    scores.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    print(scores)
    for i in range(n):
        if scores[i][0] + scores[i][1] + scores[i][2] > scores[k - 1][0] + scores[k - 1][1] + scores[k - 1][2]:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    scores = [0] * N
    for i in range(N):
        scores[i] = sum(map(int, input().split()))
    scores.sort(reverse=True)
    print("Yes" if scores[K - 1] > 0 else "No")

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]

    # print(N, K)
    # print(P)

    # A = [0] * N
    # for i in range(N):
    #     A[i] = P[i][0] + P[i][1] + P[i][2]
    # print(A)

    # B = sorted(A, reverse=True)
    # print(B)

    # for i in range(N):
    #     if B.index(A[i]) + 1 > K:
    #         print('No')
    #     else:
    #         print('Yes')

    # for i in range(N):
    #     if B.index(A[i]) + 1 > K:
    #         print('No')
    #     else:
    #         print('Yes')

    # for i in range(N):
    #     if B.index(A[i]) + 1 > K:
    #         print('No')
    #     else:
    #         print('Yes')

    # for i in range(N):
    #     if B.index(A[i]) + 1 > K:
    #         print('No')
    #     else:
    #         print('Yes')

    # for i in range(N):
    #     if B.index(A[i]) + 1 > K:
    #         print('No')
    #     else:
    #         print('Yes')

    # for i in range(N):
    #     if B.index(A[i]) + 1 > K:
    #         print('No')
    #     else:
    #         print('Yes')

    # for i in range(N):
    #     if B.index(A[i]) + 1 > K:
    #         print('No')
    #     else:
    #         print('Yes')

    # for i in range(N):
    #     if B.index(A[i]) + 1 > K:
    #         print('No')
    #     else:
    #         print('Yes')

    # for i in range(N):
    #     if B.index(A[i]) + 1 > K:
    #         print('No')
    #     else:
    #         print('Yes')
    # for i in range(N):
    #     if B.index(A[i
