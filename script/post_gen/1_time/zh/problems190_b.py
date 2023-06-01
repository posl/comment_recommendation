Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, S, D = [int(x) for x in input().split()]
    X = []
    Y = []
    for i in range(N):
        x, y = [int(x) for x in input().split()]
        X.append(x)
        Y.append(y)
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 2

def main():
    n,s,d = map(int, input().split())
    for i in range(n):
        x,y = map(int, input().split())
        if x < s and y > d:
            print("Yes")
            return
    print("No")
main()

=======
Suggestion 3

def read_data():
    #读取数据
    #输入格式
    #N S D
    #X_1 Y_1
    #.
    #.
    #.
    #X_N Y_N
    #输出格式
    #如果高桥能对怪物造成伤害，打印Yes；否则，打印No。
    #返回值
    #N:法术数量
    #S:伤害时间
    #D:伤害力度
    #X:法术施展时间列表
    #Y:法术伤害力度列表
    N,S,D = map(int,input().split())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    return N,S,D,X,Y

=======
Suggestion 4

def solution():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print("Yes")
            return
    print("No")

=======
Suggestion 5

def main():
    n, s, d = map(int, input().split())
    for i in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def solve():
    N, S, D = map(int, input().split())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    for i in range(N):
        if X[i] < S and Y[i] > D:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 7

def read_ints():
    return list(map(int,input().split()))

=======
Suggestion 8

def judge():
    n, s, d = map(int, input().split())
    for i in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            print('Yes')
            return
    print('No')
    return

judge()

=======
Suggestion 9

def isdamage(x,y,s,d):
    if x < s and y > d:
        return True
    else:
        return False
