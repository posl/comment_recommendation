Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,m,x,y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.sort()
    y_list.sort()
    if x < y and x_list[-1] < y and y_list[0] >= y:
        print("No War")
    else:
        print("War")

=======
Suggestion 2

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.append(X)
    y.append(Y)
    x.sort()
    y.sort()
    if x[-1] < y[0]:
        print('No War')
    else:
        print('War')

=======
Suggestion 3

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    for Z in range(X + 1, Y + 1):
        if max(x) < Z and min(y) >= Z:
            print('No War')
            return
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
    if x_list[-1] < y_list[0]:
        print("No War")
    else:
        print("War")

=======
Suggestion 5

def war_or_peace(N, M, X, Y, x, y):
    if max(x) < min(y) and X < min(y) and max(x) < Y:
        return 'war'
    else:
        return 'peace'

=======
Suggestion 6

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    z = x + 1
    while z <= y:
        if max(x_list) < z and min(y_list) >= z:
            print('No War')
            exit()
        z += 1
    print('War')

=======
Suggestion 7

def main():
    n,m,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    for i in range(x+1,y+1):
        if max(a) < i and min(b) >= i:
            print('No War')
            exit()
    print('War')
    return

=======
Suggestion 8

def main():
    n,m,x,y = map(int,input().split())
    xs = list(map(int,input().split()))
    ys = list(map(int,input().split()))
    xs.append(x)
    ys.append(y)
    xs.sort()
    ys.sort()
    if xs[-1] < ys[0]:
        print("No War")
    else:
        print("War")

=======
Suggestion 9

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
