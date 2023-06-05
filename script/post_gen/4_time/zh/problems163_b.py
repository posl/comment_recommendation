Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if N < sum(A):
        print(-1)
    else:
        print(N-sum(A))

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(m):
        sum += a[i]
    if sum <= n:
        print(n - sum)
    else:
        print(-1)

=======
Suggestion 3

def solve(n, m, a):
    if n < sum(a):
        return -1
    else:
        return n - sum(a)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    total = sum(A)

    if total > N:
        print(-1)
    else:
        print(N - total)

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    if sum(a) > n:
        print(-1)
    else:
        print(n - sum(a))

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    if sum_a > n:
        print(-1)
    else:
        print(n - sum_a)
main()

=======
Suggestion 8

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    if sum(a) > n:
        print(-1)
    else:
        print(n-sum(a))

=======
Suggestion 9

def main():
    # 读入数据
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 处理数据
    # 如果作业总天数大于假期天数，直接返回-1
    if sum(A) > N:
        print(-1)
        return
    # 如果作业总天数小于等于假期天数，输出假期天数减去作业总天数
    else:
        print(N - sum(A))
        return

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    if sum(a) <= n:
        print(0)
        return
    for i in range(m):
        if sum(a[:i]) <= n:
            print(i)
            return
    print(-1)
