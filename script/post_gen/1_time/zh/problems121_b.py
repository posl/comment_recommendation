Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m,c = map(int,input().split())
    b = list(map(int,input().split()))
    a = [list(map(int,input().split())) for _ in range(n)]
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

def solve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        sum = C
        for j in range(M):
            sum += A[i][j] * B[j]
        if sum > 0:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        tmp = 0
        for j in range(M):
            tmp += A[i][j] * B[j]
        if tmp + C > 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N,M,C = map(int,input().split())
    B = list(map(int,input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int,input().split())))
    count = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j]*B[j]
        if sum + C > 0:
            count += 1
    print(count)

=======
Suggestion 5

def solve():
    N, M, C = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    count = 0
    for a in A:
        sum = C
        for i in range(M):
            sum += a[i] * B[i]
        if sum > 0:
            count += 1

    print(count)

solve()

=======
Suggestion 6

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
Suggestion 7

def solve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        tmp = 0
        for j in range(M):
            tmp += A[i][j] * B[j]
        if tmp + C > 0:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N,M,C = map(int,input().split())
    B = list(map(int,input().split()))
    A = [list(map(int,input().split())) for i in range(N)]
    count = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j]*B[j]
        if sum + C > 0:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        if sum([a[i][j] * b[j] for j in range(m)]) + c > 0:
            cnt += 1
    print(cnt)

=======
Suggestion 10

def solve():
    N,M,C = map(int,input().split())
    B = list(map(int,input().split()))
    A = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        tmp = 0
        for j in range(M):
            tmp += A[i][j] * B[j]
        tmp += C
        if tmp > 0:
            cnt += 1
    print(cnt)
