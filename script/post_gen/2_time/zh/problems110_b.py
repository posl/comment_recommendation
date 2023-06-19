Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def war_or_peace(N, M, X, Y, x_list, y_list):
    for Z in range(X + 1, Y + 1):
        if max(x_list) < Z and min(y_list) >= Z:
            return '无战争'
    return '战争'

=======
Suggestion 2

def main():
    n,m,x,y = map(int, input().split())
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
    x_list.sort()
    y_list.append(y)
    y_list.sort()

    if x_list[-1] < y_list[0]:
        print("No War")
    else:
        print("War")

=======
Suggestion 5

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
Suggestion 6

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    x_list.append(x)
    y_list.append(y)

    x_list.sort()
    y_list.sort()

    if x_list[-1] < y_list[0] and x_list[-1] < y:
        print("No War")
    else:
        print("War")

=======
Suggestion 7

def judge():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    for i in range(X + 1, Y + 1):
        if max(x) < i and min(y) >= i:
            print("No War")
            return
    print("War")

judge()

=======
Suggestion 8

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    y_list.append(y)
    y_list.sort()
    if x_list[-1] < y_list[0]:
        print('No War')
    else:
        print('War')
