Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    if N < sum(A):
        print(-1)
    else:
        print(N-sum(A))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(M):
        sum += A[i]
    if sum > N:
        print(-1)
    else:
        print(N - sum)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(N-sum(A) if N>=sum(A) else -1)

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))

    if sum(A) > N:
        print(-1)
    else:
        print(N - sum(A))

main()

=======
Suggestion 5

def solve(n,m,a):
    if n < sum(a):
        return -1
    return n - sum(a)
n,m = map(int,input().split())
a = list(map(int,input().split()))
print(solve(n,m,a))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) > N:
        print(-1)
    else:
        print(N - sum(A))

=======
Suggestion 7

def get_input():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    return n, m, a

=======
Suggestion 8

def solve():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) > N:
        print(-1)
    else:
        print(N-sum(A))

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    sum_a = sum(a)
    if sum_a > n:
        print(-1)
    else:
        print(n - sum_a)

=======
Suggestion 10

def main():
    # 读入数据
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 计算完成作业所需的总天数
    total = sum(A)

    # 计算可以出去玩的天数
    if N >= total:
        print(N - total)
    else:
        print(-1)
