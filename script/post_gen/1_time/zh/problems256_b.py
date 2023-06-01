Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int,input().split()))
    P = 0
    for i in range(N):
        P += A[i] - 1
    print(P)

=======
Suggestion 2

def run():
    N = int(input())
    A = list(map(int, input().split()))

    P = 0
    blocks = [0] * 4

    for a in A:
        blocks[0] += 1
        blocks[a] += 1
        P += blocks[a - 1]
        blocks[a - 1] = 0

    print(P)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        p += 1
        if a[i] == 1:
            p += 1
        elif a[i] == 2:
            p += 2
        elif a[i] == 3:
            p += 3
        else:
            p += 4
    print(p)

=======
Suggestion 4

def main():
    # n = int(input())
    # a = list(map(int, input().split()))
    n = 10
    a = [2, 2, 4, 1, 1, 1, 4, 2, 2, 1]
    p = 0
    for i in range(n):
        p += a[i] - 1
        p %= 4
    print(p)

=======
Suggestion 5

def baseball_game(N, A):
    P = 0
    for i in range(N):
        #print('i=', i)
        #print('P=', P)
        #print('A[i]=', A[i])
        #print('A=', A)
        if i == 0:
            A[0] += 1
        else:
            A[0] += 1
            for j in range(i):
                if A[j] + A[i] > 4:
                    P += 1
                    A[j] = 0
                else:
                    A[j] += A[i]
        #print('A=', A)
        #print('P=', P)
        #print('------------------')
    print(P)
    return P

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i] - 1
    print(P)

main()

=======
Suggestion 7

def main():
    # 读取输入
    N = int(input())
    A = list(map(int, input().split()))

    # 初始化
    P = 0
    # 4个方块
    squares = [0] * 4

    # 模拟
    for i in range(N):
        # 在0号方块放置一个棋子
        squares[0] += 1
        # 移动棋子
        for j in range(4):
            # 移动
            squares[j] += A[i]
            # 如果目标方块不存在
            if squares[j] >= 4:
                # 移除棋子
                squares[j] = 0
                # P加1
                P += 1
    # 输出
    print(P)

=======
Suggestion 8

def problems256_b():
    return None

=======
Suggestion 9

def problem256_b():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    for i in range(n):
        if a[i] == 1:
            p += 1
        elif a[i] == 2:
            p += 0
        elif a[i] == 3:
            p += 2
        elif a[i] == 4:
            p += 1
    print(p)

=======
Suggestion 10

def main():
    # N = 4
    # A = [1,1,3,2]
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i] - 1
    print(P)
