Synthesizing 10/10 solutions

=======
Suggestion 1

def add_b(a,b):
    if len(a) != len(b):
        return None
    else:
        l = len(a)
        c = []
        for i in range(l):
            c.append(a[i]+b[i])
        return c

=======
Suggestion 2

def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    return N, A, B, C

=======
Suggestion 3

def main():
    # 读取输入
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    # 计算满意度积分
    result = 0
    for i in range(n):
        result += b[a[i] - 1]
        if i < n - 1 and a[i + 1] - a[i] == 1:
            result += c[a[i] - 1]

    # 打印输出
    print(result)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        sum += b[a[i]-1]
        if i < n-1 and a[i+1] == a[i]+1:
            sum += c[a[i]-1]
    print(sum)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    sum = 0
    for i in range(n):
        sum += b[a[i]-1]
        if i != n-1 and a[i] + 1 == a[i+1]:
            sum += c[a[i]-1]
    print(sum)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    s = 0
    for i in range(n):
        s += b[a[i] - 1]
        if i < n - 1 and a[i + 1] == a[i] + 1:
            s += c[a[i] - 1]

    print(s)

=======
Suggestion 7

def get_sum(N, A, B, C):
    sum = 0
    for i in range(N):
        sum += B[A[i]-1]
        if i < N-1 and A[i+1]-A[i] == 1:
            sum += C[A[i]-1]
    return sum

=======
Suggestion 8

def main():
    N = int(input())
    A = input().split()
    B = input().split()
    C = input().split()
    satisfaction = 0
    for i in range(N):
        satisfaction += int(B[i])
        if i < N-1 and int(A[i+1]) == int(A[i]) + 1:
            satisfaction += int(C[i])
    print(satisfaction)

=======
Suggestion 9

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = 0
    for i in range(n):
        ans += b[a[i]-1]
        if i < n-1 and a[i] + 1 == a[i+1]:
            ans += c[a[i]-1]
    print(ans)

=======
Suggestion 10

def read_int():
    return int(input())
