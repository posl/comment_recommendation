Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.append(x)
    y_list.append(y)
    x_list.sort()
    y_list.sort()
    if x_list[-1] < y_list[0] and x < y:
        print('No War')
    else:
        print('War')

=======
Suggestion 2

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    if max(x_list) < min(y_list) and x < min(y_list) and max(x_list) < y:
        print('No War')
    else:
        print('War')

=======
Suggestion 3

def main():
    n, m, x, y = map(int, input().split())
    x = x + 1
    y = y - 1
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.append(x)
    y_list.append(y)
    x_list.sort()
    y_list.sort()
    if x_list[-1] > y_list[0]:
        print('War')
    else:
        print('No War')

=======
Suggestion 4

def main():
    n,m,x,y = map(int,input().split())
    x_list = list(map(int,input().split()))
    y_list = list(map(int,input().split()))
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
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    for z in range(x + 1, y + 1):
        if max(x_list) < z and min(y_list) >= z:
            print("No War")
            return
    print("War")

=======
Suggestion 6

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    for z in range(x+1, y+1):
        if max(x_list) < z and min(y_list) >= z:
            print("No War")
            return

    print("War")

main()

=======
Suggestion 7

def main():
    N,M,X,Y = map(int, input().split())
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
Suggestion 8

def main():
    n,m,x,y = map(int,input().split())
    x_list = list(map(int,input().split()))
    y_list = list(map(int,input().split()))
    for i in range(x+1,y+1):
        if i in x_list and i in y_list:
            print("No War")
            break
    else:
        print("War")

=======
Suggestion 9

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.sort()
    y.sort()
    x_max = x[N-1]
    y_min = y[0]
    if x_max >= y_min:
        print("War")
    else:
        if X < x_max < Y and X < y_min < Y:
            print("No War")
        else:
            print("War")

=======
Suggestion 10

def readinput():
    n,m,x,y=map(int,input().split())
    xlist=list(map(int,input().split()))
    ylist=list(map(int,input().split()))
    return n,m,x,y,xlist,ylist
