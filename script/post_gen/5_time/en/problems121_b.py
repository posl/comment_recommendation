Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += a[i][j] * b[j]
        if sum + c > 0:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        sum = c
        for j in range(m):
            sum += a[i][j] * b[j]
        if sum > 0:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        if sum([a[i][j] * b[j] for j in range(m)]) + c > 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def solve():
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
        if s + c > 0:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(N)]
    result = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j] * B[j]
        if sum + C > 0:
            result += 1
    print(result)

=======
Suggestion 6

def solve(N, M, C, B, A):
    count = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j] * B[j]
        if sum + C > 0:
            count += 1
    return count

=======
Suggestion 7

def main():
    N,M,C = map(int,input().split())
    B = list(map(int,input().split()))
    A = [list(map(int,input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        if sum([A[i][j]*B[j] for j in range(M)]) + C > 0:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    # input
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    # compute
    ans = 0
    for a in A:
        if sum([a[i]*B[i] for i in range(M)]) + C > 0:
            ans += 1

    # output
    print(ans)

=======
Suggestion 9

def solve_problem():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        if sum([A[i][j] * B[j] for j in range(M)]) + C > 0:
            result += 1
    print(result)
