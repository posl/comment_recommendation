Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    x_max = max(x)
    y_min = min(y)

    if X < Y and x_max < y_min and X < y_min and y_min <= Y:
        print('No War')
    else:
        print('War')

=======
Suggestion 3

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
Suggestion 4

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.append(x)
    y_list.append(y)
    if max(x_list) < min(y_list):
        print("No War")
    else:
        print("War")

=======
Suggestion 5

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
Suggestion 6

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    x_list.append(x)
    y_list.append(y)

    x_max = max(x_list)
    y_min = min(y_list)

    if x_max < y_min:
        print("No War")
    else:
        print("War")

=======
Suggestion 7

def main():
    n, m, x, y = map(int, input().split())
    x_max = max(list(map(int, input().split())))
    y_min = min(list(map(int, input().split())))
    if x_max < y_min and x < y_min and y_min <= y:
        print('No War')
    else:
        print('War')

=======
Suggestion 8

def main():
    N,M,X,Y = map(int,input().split())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))
    x_max = max(x)
    y_min = min(y)
    if X < y_min and y_min <= Y and x_max < y_min:
        print("No War")
    else:
        print("War")

=======
Suggestion 9

def main():
    N,M,X,Y = map(int,input().split())
    x_list = list(map(int,input().split()))
    y_list = list(map(int,input().split()))
    x_list.sort()
    y_list.sort()
    if x_list[-1] < y_list[0] and X < y_list[0] and y_list[0] <= Y:
        print("No War")
    else:
        print("War")
main()

=======
Suggestion 10

def main():
    n, m, x, y = map(int, input().split())
    x = sorted(list(map(int, input().split())))
    y = sorted(list(map(int, input().split())))
    if x[-1] < y[0] and x[-1] < y[0] and x[-1] < y[0]:
        if x[-1] < y[0] and x[-1] < y[0] and x[-1] < y[0]:
            print("No War")
        else:
            print("War")
    else:
        print("War")
