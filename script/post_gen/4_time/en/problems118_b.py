Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    foods = set(range(1, M + 1))
    for _ in range(N):
        foods &= set(map(int, input().split()[1:]))
    print(len(foods))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, M + 1):
        for j in range(N):
            if i not in A[j][1:]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    foods = [0] * m
    for i in range(n):
        k, *a = map(int, input().split())
        for j in range(k):
            foods[a[j] - 1] += 1
    print(sum(1 for i in foods if i == n))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    ans = 0
    for i in range(1, M + 1):
        cnt = 0
        for j in range(N):
            if i in A[j][1:]:
                cnt += 1
        if cnt == N:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    S = set(range(1, M + 1))
    for _ in range(N):
        _, *A = map(int, input().split())
        S &= set(A)
    print(len(S))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    foods = [0] * M
    for _ in range(N):
        a = list(map(int, input().split()))
        for i in range(1, a[0] + 1):
            foods[a[i] - 1] += 1
    print(foods.count(N))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    ans = 0
    for i in range(n):
        k, *a = map(int, input().split())
        for j in range(m):
            if j+1 in a:
                ans += 1
                break
    print(m - ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    foods = [set() for _ in range(M)]
    for i in range(N):
        K, *A = map(int, input().split())
        for a in A:
            foods[a-1].add(i)
    ans = 0
    for f in foods:
        if len(f) == N:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = [0]*M
    for i in range(N):
        K, *a = map(int, input().split())
        for j in a:
            A[j-1] += 1
    print(A.count(N))

=======
Suggestion 10

def getInput():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    return N, M, A
