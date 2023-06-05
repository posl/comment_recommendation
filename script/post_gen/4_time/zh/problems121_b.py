Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m,c = map(int,input().split())
    b = list(map(int,input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    cnt = 0
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += a[i][j]*b[j]
        if tmp + c > 0:
            cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n,m,c = map(int,input().split())
    b = list(map(int,input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
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

def solve():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(n):
        tmp = c
        for j in range(m):
            tmp += a[i][j] * b[j]
        if tmp > 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n,m,c = map(int,input().split())
    b = list(map(int,input().split()))
    a = [list(map(int,input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += a[i][j]*b[j]
        tmp += c
        if tmp > 0:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    # N M C = map(int, input().split())
    # B = list(map(int, input().split()))
    # A = [list(map(int, input().split())) for _ in range(N)]
    N = 5
    M = 2
    C = -4
    B = [-2, 5]
    A = [[100, 41], [100, 40], [-3, 0], [-6, -2], [18, -13]]
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

def answer():
    N,M,C = map(int, input().split())
    B = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

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
Suggestion 7

def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        if sum([a * b for a, b in zip(A[i], B)]) + C > 0:
            count += 1
    print(count)

=======
Suggestion 8

def solve():
    n,m,c=map(int,input().split())
    b=list(map(int,input().split()))
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
    ans=0
    for i in range(n):
        tmp=0
        for j in range(m):
            tmp+=a[i][j]*b[j]
        if tmp+c>0:
            ans+=1
    print(ans)

solve()

=======
Suggestion 9

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
            sum += b[j] * a[i][j]
        sum += c
        if sum > 0:
            count += 1
    print(count)

=======
Suggestion 10

def solve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]

    count = 0
    for i in range(N):
        total = 0
        for j in range(M):
            total += A[i][j]*B[j]
        total += C
        if total > 0:
            count += 1

    print(count)
