Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        a = list(map(int, input().split()))
        if sum([a[j]*b[j] for j in range(m)]) + c > 0:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    ans = 0
    for _ in range(N):
        A = list(map(int, input().split()))
        if sum(a * b for a, b in zip(A, B)) + C > 0:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = list(map(int, input().split()))
        if sum([i*j for i,j in zip(a,b)]) + c > 0:
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
    A = [list(map(int, input().split())) for i in range(N)]
    cnt = 0
    for i in range(N):
        if sum([a*b for a, b in zip(A[i], B)])+C > 0:
            cnt += 1
    print(cnt)

=======
Suggestion 7

def main():
    # input
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]

    # compute
    ans = 0
    for i in range(N):
        if sum(A[i][j]*B[j] for j in range(M)) + C > 0:
            ans += 1

    # output
    print(ans)

=======
Suggestion 8

def main():
    #input
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]

    #compute
    ans = 0
    for i in range(N):
        if sum([A[i][j] * B[j] for j in range(M)]) + C > 0:
            ans += 1

    #output
    print(ans)

=======
Suggestion 9

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    print(sum([1 for a in A if sum([a[i]*b for i, b in enumerate(B)])+C > 0]))

=======
Suggestion 10

def main():
    N, M, C = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    print(sum([1 for a in A if sum([a[i] * B[i] for i in range(M)]) + C > 0]))
