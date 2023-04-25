Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        A = list(map(int, input().split()))
        if sum([a * b for a, b in zip(A, B)]) + C > 0:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = list(map(int, input().split()))
        if sum([a[j] * b[j] for j in range(m)]) + c > 0:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = list(map(int, input().split()))
        if sum([ai*bi for ai, bi in zip(a, b)]) + c > 0:
            count += 1
    print(count)

=======
Suggestion 4

def solve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    ans = 0
    for _ in range(N):
        A = list(map(int, input().split()))
        if sum(a * b for a, b in zip(A, B)) + C > 0:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for a in A:
        if sum([x*y for x, y in zip(a, B)]) + C > 0:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        if sum([A[i][j] * B[j] for j in range(M)]) + C > 0:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        s = 0
        for j in range(m):
            s += a[i][j] * b[j]
        s += c
        if s > 0:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        if sum([a[i][j] * b[j] for j in range(m)]) + c > 0:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [[0 for i in range(M)] for j in range(N)]
    for i in range(N):
        A[i] = list(map(int, input().split()))
    count = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j] * B[j]
        if sum + C > 0:
            count += 1
    print(count)
