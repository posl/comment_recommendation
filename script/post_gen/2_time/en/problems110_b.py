Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M, X, Y = [int(x) for x in input().split()]
    x = [int(x) for x in input().split()]
    y = [int(x) for x in input().split()]
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
    if x_max < y_min and x_max < Y and X < y_min:
        print("No War")
    else:
        print("War")

main()

=======
Suggestion 3

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) < min(y) and max(x) < Y and X < min(y):
        print("No War")
    else:
        print("War")

=======
Suggestion 4

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    x_max = max(x)
    y_min = min(y)

    if x_max < y_min:
        if X < y_min <= Y:
            print("No War")
        else:
            print("War")
    else:
        print("War")

=======
Suggestion 5

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_max = max(x_list)
    y_min = min(y_list)
    if x_max < y_min and x < y_min and x_max < y:
        print('No War')
    else:
        print('War')

=======
Suggestion 6

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.sort()
    y.sort()
    print("War" if x[-1] >= y[0] or x[-1] >= Y or y[0] <= X else "No War")

=======
Suggestion 7

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
Suggestion 8

def main():
    #input
    NMXY = input().split()
    x = input().split()
    y = input().split()
    N = int(NMXY[0])
    M = int(NMXY[1])
    X = int(NMXY[2])
    Y = int(NMXY[3])
    #compute
    x.sort()
    y.sort()
    x = list(map(int, x))
    y = list(map(int, y))
    if x[N-1] < y[0] and X < y[0] and x[N-1] < Y:
        print('No War')
    else:
        print('War')
    #output

=======
Suggestion 9

def main():
    # read input
    n, m, x, y = map(int, input().split())
    xa = list(map(int, input().split()))
    ya = list(map(int, input().split()))
    
    # determine war or no war
    if max(xa) >= min(ya) or max(xa) >= y or min(ya) <= x:
        print("War")
    else:
        print("No War")

main()
