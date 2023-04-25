Synthesizing 10/10 solutions (Duplicates hidden)

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
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.append(x)
    b.append(y)
    a.sort()
    b.sort()
    if a[-1] >= b[0]:
        print("War")
    else:
        print("No War")

=======
Suggestion 3

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    x_max = max(x)
    y_min = min(y)

    if X < y_min and x_max < Y:
        for z in range(x_max + 1, y_min + 1):
            if X < z <= Y:
                print('No War')
                break
        else:
            print('War')
    else:
        print('War')

main()

=======
Suggestion 4

def main():
    n, m, x, y = map(int, input().split())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))
    xs.append(x)
    ys.append(y)
    xs.sort()
    ys.sort()
    if xs[-1] < ys[0]:
        print('No War')
    else:
        print('War')

=======
Suggestion 5

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    if (max(x) < min(y)) and (max(x) < Y) and (max(y) > X):
        print("No War")
    else:
        print("War")

=======
Suggestion 6

def main():
    #N, M, X, Y = map(int, input().split())
    #x = list(map(int, input().split()))
    #y = list(map(int, input().split()))
    N, M, X, Y = 5, 3, 6, 8
    x = [-10, 3, 1, 5, -100]
    y = [100, 6, 14]
    x.sort()
    y.sort()
    if x[-1] < y[0] and x[-1] < Y and y[0] > X:
        print("No War")
    else:
        print("War")

main()

=======
Suggestion 7

def main():
    n, m, x, y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    war = False
    for z in range(x+1, y+1):
        if all([x < z for x in x_list]) and all([z <= y for y in y_list]):
            war = True
            break
    print("War" if war else "No War")

=======
Suggestion 8

def main():
    # input
    NMXY = input()
    NMXY = NMXY.split(" ")
    N = int(NMXY[0])
    M = int(NMXY[1])
    X = int(NMXY[2])
    Y = int(NMXY[3])
    x = input()
    x = x.split(" ")
    x = list(map(int, x))
    y = input()
    y = y.split(" ")
    y = list(map(int, y))
    
    # process
    war = "No War"
    x_max = max(x)
    y_min = min(y)
    for z in range(X+1, Y+1):
        if x_max < z and z <= y_min:
            war = "War"
            break
    
    # output
    print(war)

=======
Suggestion 9

def main():
    # Read data
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    # Check conditions
    if max(x) < min(y) and max(x) < Y and X < min(y):
        print("No War")
    else:
        print("War")
