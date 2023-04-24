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
        if all(i in a for a in A):
            ans += 1
    print(ans)

=======
Suggestion 3

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
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(1, M+1):
        for j in range(N):
            if i not in A[j][1:]:
                break
        else:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    foods = [0] * M
    for i in range(N):
        K, *A = map(int, input().split())
        for j in range(K):
            foods[A[j] - 1] += 1
    print(foods.count(N))

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = [0] * m
    for _ in range(n):
        for i in map(int, input().split()[1:]):
            a[i - 1] += 1
    print(sum(1 for i in a if i == n))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    ans = 0
    for i in range(n):
        a = list(map(int, input().split()))
        if a[0] == m:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = [set(map(int, input().split()[1:])) for _ in range(N)]
    print(sum(all(i in A[j] for j in range(N)) for i in range(1, M+1)))

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    D = {}
    for i in range(N):
        K, *A = map(int, input().split())
        for a in A:
            if a in D:
                D[a] += 1
            else:
                D[a] = 1
    print(len([i for i in D.values() if i == N]))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    foods = []
    for _ in range(N):
        K, *A = list(map(int, input().split()))
        foods.append(set(A))
    ans = 0
    for i in range(1, M+1):
        if all(i in food for food in foods):
            ans += 1
    print(ans)
