Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    print(*b)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    print(' '.join(map(str, b)))

=======
Suggestion 3

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    print(' '.join(map(str, b)))

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    print(*b)

=======
Suggestion 5

def main():
    # N = int(input())
    # A = list(map(int, input().split()))
    N = 8
    A = [8, 2, 7, 3, 4, 5, 6, 1]
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(B)

=======
Suggestion 6

def main():
    # 读入数据
    n = int(input())
    a = list(map(int, input().split()))
    # 从后往前遍历
    ans = []
    for i in range(n-1, -1, -1):
        ans.insert(a[i]-1, i+1)
    # 输出
    print(*ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i+1
    print(*b)

main()

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        ans.insert(a[i]-1, i+1)
    print(*ans)
