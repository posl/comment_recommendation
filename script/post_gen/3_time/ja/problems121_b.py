Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        A = list(map(int, input().split()))
        if sum([A[j] * B[j] for j in range(M)]) + C > 0:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        A = list(map(int, input().split()))
        sum = 0
        for j in range(M):
            sum += A[j] * B[j]
        sum += C
        if sum > 0:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        tmp = 0
        for j in range(M):
            tmp += A[i][j] * B[j]
        tmp += C
        if tmp > 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        if sum([A[i][j] * B[j] for j in range(M)]) + C > 0:
            ans += 1
    print(ans)

=======
Suggestion 5

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
Suggestion 6

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        if sum([A[i][j] * B[j] for j in range(M)]) + C > 0:
            cnt += 1

    print(cnt)

=======
Suggestion 7

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    print(sum(1 for a in A if sum(b * c for b, c in zip(B, a)) + C > 0))

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    AC = 0
    for i in range(N):
        if sum([A[i][j]*B[j] for j in range(M)]) + C > 0:
            AC += 1
    print(AC)

=======
Suggestion 10

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [[int(i) for i in input().split()] for j in range(N)]
    cnt = 0
    for i in range(N):
        if sum([A[i][j] * B[j] for j in range(M)]) + C > 0:
            cnt += 1
    print(cnt)
