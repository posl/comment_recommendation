Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        a[i] -= 1
        p += a[i] // 4
        a[i] %= 4
        if a[i] == 0:
            continue
        p += 1
        if i < n - 1:
            a[i + 1] -= a[i]
    print(p)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        x = A[i] - 1
        P += x
    print(P)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        if A[i] == 1:
            P += 0
        elif A[i] == 2:
            P += 1
        elif A[i] == 3:
            P += 2
        elif A[i] == 4:
            P += 3
    print(P)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i] - 1
    print(P)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        p += a[i] - 1
    print(p)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i] - 1
        P %= 4
    print(P)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i] - 1
    print(P)
main()

=======
Suggestion 8

def problem256_b():
    # 读取输入
    N = int(input())
    A = [int(x) for x in input().split()]
    # 棋子位置
    chess = [0 for _ in range(4)]
    # 移除棋子数量
    P = 0
    # 操作
    for i in range(N):
        # 在0号方格放一个棋子
        chess[0] += 1
        # 将每个棋子在方格上向前推进A[i]个方格
        for j in range(4):
            if chess[j] > 0:
                if j + A[i] < 4:
                    chess[j + A[i]] += chess[j]
                P += chess[j]
                chess[j] = 0
    print(P)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        p += a[i] - 1
        p %= 4
    print(p)
