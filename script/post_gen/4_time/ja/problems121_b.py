Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    cnt = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j] * B[j]
        if sum + C > 0:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += a[i][j] * b[j]
        if tmp + c > 0:
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
        sum = 0
        for j in range(m):
            sum += a[i][j] * b[j]
        sum += c
        if sum > 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        a = list(map(int, input().split()))
        sum = 0
        for j in range(m):
            sum += a[j] * b[j]
        sum += c
        if sum > 0:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(N)]
    count = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j] * B[j]
        sum += C
        if sum > 0:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for a in A:
        sum = 0
        for i in range(M):
            sum += a[i] * B[i]
        sum += C
        if sum > 0:
            count += 1

    print(count)

=======
Suggestion 7

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        sum = c
        for j in range(m):
            sum += a[i][j] * b[j]
        if sum > 0:
            cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    N,M,C = map(int,input().split())
    B = list(map(int,input().split()))
    A = [list(map(int,input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        tmp = 0
        for j in range(M):
            tmp += A[i][j]*B[j]
        tmp += C
        if tmp > 0:
            ans += 1
    print(ans)

=======
Suggestion 9

def main():
    N,M,C = map(int,input().split())
    B = list(map(int,input().split()))
    A = [list(map(int,input().split())) for i in range(N)]
    count = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j] * B[j]
        if sum + C > 0:
            count += 1
    print(count)

=======
Suggestion 10

def solve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))

    cnt = 0
    for _ in range(N):
        A = list(map(int, input().split()))
        if sum([a*b for a,b in zip(A,B)]) + C > 0:
            cnt += 1

    print(cnt)
