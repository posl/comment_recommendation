Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    # 输入
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for _ in range(N)]
    # 计算
    ans = 0
    for i in range(N):
        if sum([A[i][j]*B[j] for j in range(M)]) + C > 0:
            ans += 1
    # 输出
    print(ans)

solve()

=======
Suggestion 2

def main():
    # 读取输入
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]

    # 计算
    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += a[i][j] * b[j]
        if tmp + c > 0:
            ans += 1

    # 输出
    print(ans)

=======
Suggestion 3

def main():
    n,m,c = map(int,input().split())
    b = list(map(int,input().split()))
    a = [list(map(int,input().split())) for _ in range(n)]
    print(a)
    print(b)
    print(c)
    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += a[i][j]*b[j]
        if tmp + c > 0:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for _ in range(n)]
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
    n, m, c = map(int, input().split())
    b_list = list(map(int, input().split()))
    a_list = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for a in a_list:
        sum = 0
        for i in range(m):
            sum += a[i] * b_list[i]
        if sum + c > 0:
            ans += 1
    print(ans)

solve()

=======
Suggestion 6

def solve(n, m, c, b, a):
    count = 0
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += a[i][j] * b[j]
        if sum + c > 0:
            count += 1
    return count

=======
Suggestion 7

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
Suggestion 8

def main():
    n,m,c = map(int,input().split())
    b = list(map(int,input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))

    count = 0
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += a[i][j] * b[j]
        if sum + c > 0:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    # 读入
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [list(map(int, input().split())) for i in range(N)]

    # 计算
    ans = 0
    for i in range(N):
        tmp = 0
        for j in range(M):
            tmp += A[i][j] * B[j]
        if tmp + C > 0:
            ans += 1

    # 输出
    print(ans)

=======
Suggestion 10

def main():
    n,m,c = map(int,input().split())
    b = list(map(int,input().split()))
    a = [list(map(int,input().split())) for i in range(n)]
    ans = 0
    for i in range(n):
        tmp = 0
        for j in range(m):
            tmp += a[i][j]*b[j]
        if tmp + c > 0:
            ans += 1
    print(ans)
