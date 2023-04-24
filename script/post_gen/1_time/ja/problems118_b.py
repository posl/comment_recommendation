Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [set(map(int, input().split()[1:])) for _ in range(N)]
    print(len(set.intersection(*A)))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, M+1):
        cnt = 0
        for j in range(N):
            if i in A[j][1:]:
                cnt += 1
        if cnt == N:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    food = [0] * M
    for _ in range(N):
        K, *A = map(int, input().split())
        for a in A:
            food[a-1] += 1
    print(food.count(N))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    food = [0] * M
    for i in range(N):
        K, *A = map(int, input().split())
        for j in range(K):
            food[A[j]-1] += 1
    print(food.count(N))

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [0] * M
    for i in range(N):
        a = list(map(int, input().split()))
        for j in range(1, a[0] + 1):
            A[a[j] - 1] += 1
    print(A.count(N))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    like = [0] * m
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(tmp[0]):
            like[tmp[j+1]-1] += 1
    print(like.count(n))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = [0] * M
    for i in range(N):
        K, *tmp = map(int, input().split())
        for j in tmp:
            A[j-1] += 1
    print(A.count(N))

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    A = [0] * M
    for i in range(N):
        K, *B = map(int, input().split())
        for b in B:
            A[b-1] += 1
    print(A.count(N))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [0 for _ in range(M + 1)]
    for i in range(N):
        for j in range(1, len(A[i])):
            B[A[i][j]] += 1
    ans = 0
    for i in range(1, M + 1):
        if B[i] == N:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    dishes = set()
    for _ in range(N):
        K, *A = map(int, input().split())
        dishes |= set(A)
    print(len(dishes))
