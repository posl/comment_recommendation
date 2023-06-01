Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(1, n):
        b[a[i - 1] - 1] += 1
    for i in b:
        print(i)

=======
Suggestion 2

def solve(n, a):
    ans = [0] * n
    for i in range(1, n):
        ans[a[i - 1] - 1] += 1
    return ans

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[a[i]] += 1
    for i in range(1, n + 1):
        print(b[i])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N - 1):
        B[A[i] - 1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(1, N):
        B[A[i] - 1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 6

def problem163_c():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n-1):
        b[a[i]-1] += 1
    for i in range(n):
        print(b[i])

problem163_c()

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0 for i in range(N)]
    for i in range(N-1):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = [0] * n
    for i in range(1, n):
        c[a[i] - 1] += 1
    for i in range(n):
        print(c[i])

main()

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(1, n):
        b[a[i] - 1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 10

def main():
    # 读入数据
    N = int(input())
    A = list(map(int, input().split()))

    # print(N, A)

    # 计算直属下级的数量
    B = [0] * N
    for i in range(1, N):
        B[A[i] - 1] += 1

    # print(B)

    # 输出结果
    for i in range(N):
        print(B[i])
