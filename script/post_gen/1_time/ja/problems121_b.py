Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    count = 0
    for i in range(N):
        A = list(map(int, input().split()))
        if sum([A[i] * B[i] for i in range(M)]) + C > 0:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    count = 0
    for i in range(N):
        A = list(map(int, input().split()))
        total = 0
        for j in range(M):
            total += A[j] * B[j]
        total += C
        if total > 0:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        A = list(map(int, input().split()))
        if sum([a*b for a, b in zip(A, B)]) + C > 0:
            cnt += 1
    print(cnt)

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
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
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
    ans = 0
    for i in range(N):
        if sum([A[i][j] * B[j] for j in range(M)]) + C > 0:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        if sum([a[i][j] * b[j] for j in range(m)]) + c > 0:
            ans += 1

    print(ans)

main()

=======
Suggestion 8

def main():
    #入力
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    #処理
    cnt = 0
    for i in range(N):
        if sum([a*b for a,b in zip(A[i],B)]) + C > 0:
            cnt += 1
    #出力
    print(cnt)
