Synthesizing 10/10 solutions

=======
Suggestion 1

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
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    count = 0
    for i in range(N):
        A = list(map(int, input().split()))
        if sum([A[j]*B[j] for j in range(M)]) + C > 0:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))

    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += a[i][j] * b[j]
        tmp += c
        if tmp > 0:
            ans += 1

    print(ans)

=======
Suggestion 5

def solve():
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
        sum += C
        if sum > 0:
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += a[i][j] * b[j]
        if sum + c > 0:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def solve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for a in A:
        if sum([a[i] * B[i] for i in range(M)]) + C > 0:
            ans += 1
    print(ans)

=======
Suggestion 8

def get_input():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    return N, M, C, B, A

=======
Suggestion 9

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(N)]
    answer = 0
    for i in range(N):
        score = 0
        for j in range(M):
            score += A[i][j] * B[j]
        if score + C > 0:
            answer += 1
    print(answer)

=======
Suggestion 10

def problem121_b():
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
