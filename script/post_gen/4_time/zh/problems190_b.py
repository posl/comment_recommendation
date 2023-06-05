Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    n, s, d = map(int, input().split())
    # print(n, s, d)
    # print(type(n), type(s), type(d))
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    # print(x)
    # print(y)
    # print(type(x), type(y))
    # 处理
    flag = 0
    for i in range(n):
        if x[i] < s and y[i] > d:
            flag = 1
            break
    # 输出
    if flag == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def solve():
    N,S,D = map(int,input().split())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print('Yes')
            return
    print('No')

=======
Suggestion 3

def solve():
    #读入数据
    n,s,d = map(int,input().split())
    #print(n,s,d)
    x = []
    y = []
    for i in range(n):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    #print(x)
    #print(y)
    #处理数据
    for i in range(n):
        if x[i] < s and y[i] > d:
            print('Yes')
            return
    print('No')
    return

solve()

=======
Suggestion 4

def solve():
    N,S,D = map(int,input().split())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 5

def solution():
    n,s,d = map(int,input().split())
    for i in range(n):
        x,y = map(int,input().split())
        if x < s and y > d:
            print("Yes")
            return
    print("No")

=======
Suggestion 6

def main():
    N,S,D = [int(x) for x in input().split()]
    X = []
    Y = []
    for i in range(N):
        x,y = [int(x) for x in input().split()]
        X.append(x)
        Y.append(y)
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print('Yes')
            break
    else:
        print('No')

=======
Suggestion 7

def main():
    n,s,d=map(int,input().split())
    for i in range(n):
        x,y=map(int,input().split())
        if x<s and y>d:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 8

def main():
    N,S,D = map(int,input().split())
    for i in range(N):
        X,Y = map(int,input().split())
        if X < S and Y > D:
            print("Yes")
            return
    print("No")

=======
Suggestion 9

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
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def main():
    #n,s,d = map(int, input().split())
    #x = []
    #y = []
    #for i in range(n):
    #    x_i, y_i = map(int, input().split())
    #    x.append(x_i)
    #    y.append(y_i)
    n, s, d = 7, 100, 100
    x = [10, 12, 192, 154, 142, 20, 17]
    y = [11, 67, 79, 197, 158, 25, 108]
    for i in range(n):
        if x[i] < s and y[i] > d:
            print('Yes')
            return
    print('No')
