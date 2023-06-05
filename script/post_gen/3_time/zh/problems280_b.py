Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读入数据
    n = int(input())
    s = list(map(int, input().split()))

    # 计算答案
    a = [0] * n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]

    # 打印答案
    print(' '.join(map(str, a)))

=======
Suggestion 2

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i - 1]
    print(' '.join(map(str, A)))

=======
Suggestion 3

def main():
    n = int(input())
    s = list(map(int,input().split()))
    a = [0]*n
    a[0] = s[0]
    for i in range(1,n):
        a[i] = s[i] - s[i-1]
    print(*a)

=======
Suggestion 4

def main():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i-1]
    print(*A)

=======
Suggestion 5

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = [0]*n
    a[0] = s[0]
    for i in range(1, n):
        a[i] = s[i] - s[i-1]
    print(' '.join(list(map(str, a))))

=======
Suggestion 6

def main():
    #输入
    N = int(input())
    S = list(map(int, input().split()))

    #求和
    sum = 0
    for i in range(N):
        sum += S[i]

    #求A
    A = [0] * N
    A[0] = sum // N
    for i in range(1, N):
        A[i] = 2 * S[i - 1] - A[i - 1]

    #输出
    for i in range(N):
        print(A[i], end=' ')

=======
Suggestion 7

def main():
    N = int(input())
    S = input().split()
    A = [0 for i in range(N)]
    for i in range(N):
        A[i] = int(S[i])
    for i in range(N):
        print(A[i], end=' ')
        for j in range(i+1, N):
            A[j] = A[j-1] + A[j] - A[i]
        print()

=======
Suggestion 8

def solve():
    N = int(input())
    S = list(map(int, input().split()))
    A = [0] * N
    A[0] = S[0]
    for i in range(1, N):
        A[i] = S[i] - S[i - 1]
    print(' '.join(map(str, A)))
solve()

=======
Suggestion 9

def solve(n, s):
    a = [0] * n
    for i in range(n - 1):
        a[i] = s[i] + a[i - 1]
    a[n - 1] = s[n - 1] + a[n - 2]
    return a
