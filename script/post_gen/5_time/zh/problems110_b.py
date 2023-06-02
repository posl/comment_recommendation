Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.append(X)
    y.append(Y)
    x.sort()
    y.sort()
    if x[-1] < y[0]:
        print("No War")
    else:
        print("War")

=======
Suggestion 2

def main():
    n, m, x, y = map(int, input().split())
    x_city = list(map(int, input().split()))
    y_city = list(map(int, input().split()))
    for z in range(x+1, y+1):
        if max(x_city) < z <= min(y_city):
            print("No War")
            return
    print("War")

=======
Suggestion 3

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.append(x)
    y_list.append(y)
    x_list.sort()
    y_list.sort()
    if x_list[-1] < y_list[0]:
        print('No War')
    else:
        print('War')

=======
Suggestion 4

def main():
    n, m, x, y = map(int, input().split())
    xList = list(map(int, input().split()))
    yList = list(map(int, input().split()))
    z = 0
    for i in range(x + 1, y + 1):
        if max(xList) < i and min(yList) >= i:
            z = i
            break
    if z == 0:
        print("战争")
    else:
        print("无战争")

=======
Suggestion 5

def main():
    n,m,x,y = map(int,input().split())
    x_lst = list(map(int,input().split()))
    y_lst = list(map(int,input().split()))

    for z in range(x+1,y+1):
        if max(x_lst) < z and min(y_lst) >= z:
            print("No War")
            return

    print("War")

=======
Suggestion 6

def war_or_peace():
    input1 = input("请输入N M X Y\n")
    input2 = input("请输入x_1 x_2 ... x_N\n")
    input3 = input("请输入y_1 y_2 ... y_M\n")
    input1 = input1.split()
    input2 = input2.split()
    input3 = input3.split()
    input1 = [int(i) for i in input1]
    input2 = [int(i) for i in input2]
    input3 = [int(i) for i in input3]
    x = input1[0]
    y = input1[1]
    N = input1[2]
    M = input1[3]
    input2.sort()
    input3.sort()
    if x < input2[0] and input2[0] < y and y <= input3[0]:
        print("无战争")
    else:
        print("战争")

war_or_peace()

=======
Suggestion 7

def main():
    n,m,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if x < a[-1] < b[0] and a[-1] < b[0] <= y:
        print("No War")
    else:
        print("War")

=======
Suggestion 8

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    if max(x_list) < min(y_list) and x < min(y_list) and min(y_list) <= y:
        print("No War")
    else:
        print("War")

=======
Suggestion 9

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    x.append(X)
    y.append(Y)

    x.sort()
    y.sort()

    if x[N] < y[0]:
        print('No War')
    else:
        print('War')

=======
Suggestion 10

def main():
    #输入
    n, m, x, y = map(int, input().split())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    #处理
    X.sort()
    Y.sort()
    #print(X)
    #print(Y)
    Z = [i for i in range(x+1, y+1)]
    #print(Z)
    if len(Z) == 0:
        print("战争")
    else:
        for i in Z:
            if i > X[-1] and i <= Y[0]:
                print("合法")
                break
        else:
            print("战争")
