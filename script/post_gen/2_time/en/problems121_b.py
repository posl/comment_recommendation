Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    ans = 0
    for _ in range(N):
        A = list(map(int, input().split()))
        if sum([A[i]*B[i] for i in range(M)]) + C > 0:
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
        if sum([a*b for a, b in zip(A, B)]) + C > 0:
            cnt += 1
    print(cnt)

main()

=======
Suggestion 3

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    count = 0
    for _ in range(N):
        A = list(map(int, input().split()))
        if sum(map(lambda x,y: x*y, A, B)) + C > 0:
            count += 1
    print(count)

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
    ans = 0
    for a in A:
        if sum([a[i] * B[i] for i in range(M)]) + C > 0:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        if sum([a[i][j]*b[j] for j in range(m)]) + c > 0:
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
        if sum([a*b for a, b in zip(A[i], B)]) + C > 0:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    print(sum(1 for i in A if sum(a*b for a, b in zip(A[i], B)) + C > 0))

=======
Suggestion 9

def main():
    N, M, C = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(N)]
    ans = 0
    for i in range(N):
        if sum([A[i][j] * B[j] for j in range(M)]) + C > 0:
            ans += 1
    print(ans)
