Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    x_max = max(x)
    y_min = min(y)

    if x_max < y_min and X < x_max < Y and X < y_min <= Y:
        print("No War")
    else:
        print("War")

=======
Suggestion 2

def main():
    # 標準入力からN, M, X, Yを取得する
    N, M, X, Y = map(int, input().split())
    # 標準入力からA帝国の都市の座標を取得する
    x_list = list(map(int, input().split()))
    # 標準入力からB帝国の都市の座標を取得する
    y_list = list(map(int, input().split()))

    # A帝国の都市の座標の最大値を取得する
    x_max = max(x_list)
    # B帝国の都市の座標の最小値を取得する
    y_min = min(y_list)

    # X < Z ≦ Y かつ x_1, x_2, ..., x_N < Z かつ y_1, y_2, ..., y_M ≧ Z を満たす整数Zが存在するかどうかを判定する
    if X < y_min and y_min <= Y and x_max < y_min:
        print("No War")
    else:
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

    if x_list[-1] >= y_list[0]:
        print('War')
    else:
        print('No War')

=======
Suggestion 4

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
Suggestion 5

def main():
    n,m,x,y = map(int,input().split())
    xlist = list(map(int,input().split()))
    ylist = list(map(int,input().split()))
    xlist.append(x)
    ylist.append(y)
    xlist.sort()
    ylist.sort()
    if xlist[-1] < ylist[0]:
        print("No War")
    else:
        print("War")

=======
Suggestion 6

def main():
    n, m, x, y = map(int, input().split())
    x_max = max(list(map(int, input().split())))
    y_min = min(list(map(int, input().split())))
    if x_max < y_min and x < y_min and y_min <= y:
        print("No War")
    else:
        print("War")

=======
Suggestion 7

def main():
    N, M, X, Y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    x_list.append(X)
    y_list.append(Y)

    x_max = max(x_list)
    y_min = min(y_list)

    if x_max < y_min:
        print('No War')
    else:
        print('War')

=======
Suggestion 8

def main():
    # 標準入力から値を取得してinput_lineに入れる
    input_line = input().rstrip()
    # input_lineを空白で分割して、input_lineに上書き
    N, M, X, Y = input_line.split()
    N = int(N)
    M = int(M)
    X = int(X)
    Y = int(Y)

    # 標準入力から値を取得してinput_lineに入れる
    input_line = input().rstrip()
    # input_lineを空白で分割して、input_lineに上書き
    x = input_line.split()
    x = list(map(int, x))

    # 標準入力から値を取得してinput_lineに入れる
    input_line = input().rstrip()
    # input_lineを空白で分割して、input_lineに上書き
    y = input_line.split()
    y = list(map(int, y))

    x.append(X)
    y.append(Y)

    x.sort()
    y.sort()

    if x[N] >= y[0]:
        print("War")
    else:
        print("No War")

=======
Suggestion 9

def main():
    n,m,x,y = map(int,input().split())
    x_list = list(map(int,input().split()))
    y_list = list(map(int,input().split()))

    x_list.sort()
    y_list.sort()

    if x_list[-1] < y_list[0] and x < y_list[0] and y > x_list[-1]:
        print('No War')
    else:
        print('War')

=======
Suggestion 10

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.append(x)
    y_list.append(y)
    if max(x_list) >= min(y_list):
        print('War')
    else:
        print('No War')
