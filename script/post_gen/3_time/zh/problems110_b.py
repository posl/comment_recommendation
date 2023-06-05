Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m,x,y = map(int,input().split())
    xlist = list(map(int,input().split()))
    ylist = list(map(int,input().split()))
    xlist.append(x)
    ylist.append(y)
    xlist.sort()
    ylist.sort()
    if xlist[n] < ylist[0]:
        print('No War')
    else:
        print('War')

=======
Suggestion 2

def main():
    # 输入
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    # 逻辑处理
    x.append(X)
    y.append(Y)
    x.sort()
    y.sort()

    # 输出
    if x[-1] < y[0] and x[-1] < Y and y[0] > X:
        print('No War')
    else:
        print('War')

=======
Suggestion 3

def main():
    n,m,x,y = map(int,input().split())
    x_list = list(map(int,input().split()))
    y_list = list(map(int,input().split()))
    z = x+1
    if z<=y:
        if max(x_list)<z and min(y_list)>=z:
            print('No War')
        else:
            print('War')
    else:
        print('War')

=======
Suggestion 4

def main():
    # N, M, X, Y = map(int, input().split())
    # x = list(map(int, input().split()))
    # y = list(map(int, input().split()))
    N, M, X, Y = 3, 2, 10, 20
    x = [8, 15, 13]
    y = [16, 22]
    x.sort()
    y.sort()
    if x[-1] < y[0] and X < y[0] and y[0] <= Y:
        print("No War")
    else:
        print("War")

=======
Suggestion 5

def input():
    N, M, X, Y = input().split()
    N, M, X, Y = int(N), int(M), int(X), int(Y)
    x_list = [int(x) for x in input().split()]
    y_list = [int(y) for y in input().split()]
    return N, M, X, Y, x_list, y_list

=======
Suggestion 6

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    if max(x_list) < min(y_list) and x < min(y_list) and min(y_list) <= y:
        print("No War")
    else:
        print("War")

=======
Suggestion 7

def main():
    N,M,X,Y = map(int,input().split())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    x.append(X)
    y.append(Y)
    x.sort()
    y.sort()
    if x[-1] < y[0]:
        print("No War")
    else:
        print("War")

=======
Suggestion 8

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.append(x)
    y_list.append(y)
    x_list.sort()
    y_list.sort()
    if x_list[-1] < y_list[0]:
        print("No War")
    else:
        print("War")

=======
Suggestion 9

def main():
    n, m, x, y = map(int, input().split())
    xx = list(map(int, input().split()))
    yy = list(map(int, input().split()))
    xx.append(x)
    yy.append(y)
    xx.sort()
    yy.sort()
    if xx[-1] < yy[0]:
        print('No War')
    else:
        print('War')

=======
Suggestion 10

def war_or_peace(N, M, X, Y, x_list, y_list):
    for i in range(N):
        if x_list[i] >= Y:
            return "War"
    for i in range(M):
        if y_list[i] < X:
            return "War"
    return "No War"
