Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    print((n-1)*2/(n-2))

=======
Suggestion 2

def solve():
    N = int(input())
    ans = 0
    for i in range(1,N):
        ans += 1/i
    ans = ans * N
    print("{:.11f}".format(ans))

=======
Suggestion 3

def main():
    N = int(input())
    print(N * (N - 1) / 2 / (N - 1) + 1)

=======
Suggestion 4

def main():
    N = int(input())
    print((N+1)*3/2)

=======
Suggestion 5

def main():
    n = int(input())
    print(n * (n - 1) / (n * (n - 1) / 2))

=======
Suggestion 6

def solve():
    N = int(input())
    print(sum([1/i for i in range(1, N+1)]))

=======
Suggestion 7

def main():
    N = int(input())
    print(1+sum([i*((1/N)**i) for i in range(1,N)]))

=======
Suggestion 8

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        ans += n/i
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    print(N * ((N + 1) / 2))

=======
Suggestion 10

def main():
    # 读取输入
    n = int(input())

    # 算法
    # 期望值 = 每次操作的期望值 * 操作次数
    # 每次操作的期望值 = 1 / (n - i) (i为已经有边的顶点数)
    # 操作次数 = 1 / (1 / n) = n
    # 期望值 = 1 / (n - i) * n
    # 总期望值 = sum(1 / (n - i) * n) (i = 0 to n - 1)
    #         = n * sum(1 / (n - i)) (i = 0 to n - 1)
    #         = n * sum(1 / i) (i = 1 to n)
    #         = n * H(n)
    #         = n * (ln(n) + γ + 1 / (2n) - 1 / (12n^2) + 1 / (120n^4) - 1 / (252n^6) + ...)
    #         = n * (ln(n) + γ + 1 / (2n) + O(1 / n^2))

    # 期望值 = n * (ln(n) + γ + 1 / (2n) + O(1 / n^2))
    # 期望值 = n * ln(n) + n * γ + 1 / 2 + O(1 / n)
    # 期望值 = n * ln(n) + n * γ + O(n)

    # 输出
    print(n * math.log(n) + n * 0.57721566490153286060651209008240243104215933593992 + 0.5)
