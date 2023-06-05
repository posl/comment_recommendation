Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(n - sum(a) if n >= sum(a) else -1)

=======
Suggestion 2

def solve():
    #读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    #排序
    a.sort()
    #计算结果
    result = 0
    for i in range(m):
        result += a[i]
    if result > n:
        result = -1
    else:
        result = n - result
    #输出结果
    print(result)

=======
Suggestion 3

def main():
    # 读取输入
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # 初始化
    a.sort()
    a.reverse()
    # 计算
    if sum(a) <= n:
        print(0)
    else:
        for i in range(m):
            if sum(a) - a[i] <= n:
                print(i + 1)
                break
        else:
            print(-1)

=======
Suggestion 4

def solve(n, m, a):
    if sum(a) < n:
        return -1
    return n - sum(a)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) > n:
        print(-1)
    else:
        print(n - sum(a))

=======
Suggestion 6

def solve():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    if sum(a) > n:
        print(-1)
    else:
        print(n-sum(a))

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if n < sum(a):
        print(-1)
    else:
        print(n - sum(a))

=======
Suggestion 8

def main():
    # 读取输入
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 求出总和
    sum = 0
    for i in range(M):
        sum += A[i]

    # 判断
    if sum > N:
        print(-1)
    else:
        print(N - sum)

=======
Suggestion 9

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    if sum(a) > n:
        print(-1)
        return
    print(n - sum(a))
