Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    for i in range(n):
        p += a[i] - 1
    print(p)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    squares = [0 for i in range(4)]
    for i in range(N):
        squares[0] += 1
        for j in range(4):
            if squares[j] > 0:
                squares[(j + A[i]) % 4] += squares[j]
                squares[j] = 0
        P += squares[3]
    print(P)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    P = 0
    for i in range(N):
        P += A[i] - 1
        P %= 4
    print(P)

=======
Suggestion 4

def main():
    #输入
    N = int(input())
    A = list(map(int,input().split()))
    #初始化
    P = 0
    #遍历
    for i in range(N):
        #将方格上的每个棋子向前推进A[i]个方格
        for j in range(i+1):
            #如果目标方格不存在（即x+A_i大于或等于4）的棋子，则将其移除
            if A[j] + j >= 4:
                P += 1
                A[j] = 0
            else:
                A[j] += A[i]
        #在0号方格放一个棋子，现在0号方格有一个棋子。
        A[0] += 1
    print(P)

=======
Suggestion 5

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

=======
Suggestion 6

def move(i):
    global P
    for j in range(4):
        if j + A[i] < 4:
            if field[j + A[i]] > 0:
                field[j + A[i]] += field[j]
            else:
                field[j + A[i]] = field[j]
        else:
            P += field[j]

N = int(input())
A = list(map(int, input().split()))
field = [0] * 4
P = 0
for i in range(N):
    field[0] += 1
    move(i)
print(P)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        cnt += a[i] - 1
    print(cnt)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int,input().split()))
    p = 0
    for i in range(n):
        p = p + a[i] - 1
    print(p)

=======
Suggestion 9

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = 0
    s = [0, 0, 0, 0]
    for i in range(n):
        s[a[i] - 1] += 1
        p += s[3]
        s[3] = s[2]
        s[2] = s[1]
        s[1] = s[0]
        s[0] = 0
    print(p)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    P = 0
    for i in range(N):
        P += A[i] - 1
        P %= 2
    print(P)
