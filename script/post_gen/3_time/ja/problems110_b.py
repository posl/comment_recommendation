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
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x_max = max(x)
    y_min = min(y)
    if x_max < y_min and X < y_min and y_min <= Y:
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
    x_max = max(x_list)
    y_min = min(y_list)
    if x_max < y_min:
        print('No War')
    else:
        print('War')

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
    if x_list[-1] >= y_list[0]:
        print('War')
    else:
        print('No War')

=======
Suggestion 5

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    x_list.append(x)
    y_list.append(y)

    x_max = max(x_list)
    y_min = min(y_list)

    if x_max >= y_min:
        print("War")
    else:
        print("No War")

=======
Suggestion 6

def main():
    # input
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    # compute
    x_max = max(x)
    y_min = min(y)

    # output
    if x_max < y_min and X < y_min and y_min <= Y:
        print("No War")
    else:
        print("War")

=======
Suggestion 7

def main():
    n,m,x,y = map(int, input().split())
    xlist = list(map(int, input().split()))
    ylist = list(map(int, input().split()))
    xlist.append(x)
    ylist.append(y)
    xlist.sort()
    ylist.sort()
    if xlist[-1] < ylist[0]:
        print("No War")
    else:
        print("War")

=======
Suggestion 8

def main():
    # N, M, X, Y = map(int, input().split())
    # x = list(map(int, input().split()))
    # y = list(map(int, input().split()))
    N, M, X, Y = 3, 2, 10, 20
    x = [8, 15, 13]
    y = [16, 22]
    # N, M, X, Y = 4, 2, -48, -1
    # x = [-20, -35, -91, -23]
    # y = [-22, 66]
    # N, M, X, Y = 5, 3, 6, 8
    # x = [-10, 3, 1, 5, -100]
    # y = [100, 6, 14]

    if X < Y:
        if max(x) < min(y) and X < min(y) and min(y) <= Y:
            print('No War')
        else:
            print('War')
    else:
        print('War')

=======
Suggestion 9

def main():
    n, m, x, y = map(int, input().split())
    lst_x = list(map(int, input().split()))
    lst_y = list(map(int, input().split()))
    max_x = max(lst_x)
    min_y = min(lst_y)
    if max_x < min_y and x < min_y and min_y <= y:
        print("No War")
    else:
        print("War")
main()

=======
Suggestion 10

def main():
    n,m,x,y=map(int,input().split())
    x_list=list(map(int,input().split()))
    y_list=list(map(int,input().split()))
    for i in range(x+1,y+1):
        if max(x_list)<i and min(y_list)>=i:
            print("No War")
            return
    print("War")
    return

main()
