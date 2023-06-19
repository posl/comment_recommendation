Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) <= n:
        print(n - sum(a))
    else:
        print(-1)

=======
Suggestion 2

def solve(n,m,a):
    if n < sum(a):
        return -1
    else:
        return n - sum(a)

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) > N:
        return -1
    else:
        return N - sum(A)

print(solve())

=======
Suggestion 4

def main():
    # 读取输入
    line = input()
    line = line.split()
    n = int(line[0])
    m = int(line[1])
    line = input()
    line = line.split()
    a = []
    for i in range(m):
        a.append(int(line[i]))
    # 处理
    a.sort()
    sum = 0
    for i in range(m):
        sum += a[i]
    if sum > n:
        print(-1)
    else:
        print(n - sum)

=======
Suggestion 5

def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    if sum(A) <= N:
        print(N-sum(A))
    else:
        print(-1)

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) > N:
        print(-1)
        return
    print(N - sum(A))

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(M):
        sum += A[i]
    if sum > N:
        print(-1)
    else:
        print(N - sum)

main()

=======
Suggestion 8

def solve(n, m, a):
    if n < sum(a):
        return -1
    return n - sum(a)

=======
Suggestion 9

def main():
    n,m = input().split()
    n = int(n)
    m = int(m)
    a = input().split()
    a = [int(i) for i in a]
    sum = 0
    for i in range(m):
        sum += a[i]
    if sum <= n:
        print(n-sum)
    else:
        print(-1)

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) > n:
        print(-1)
    else:
        print(n - sum(a))
