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
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) < min(y) and max(x) < Y and min(y) > X:
        print('No War')
    else:
        print('War')

=======
Suggestion 3

def main():
    N, M, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.append(X)
    B.append(Y)
    A.sort()
    B.sort()
    if A[N] < B[0]:
        print("No War")
    else:
        print("War")

=======
Suggestion 4

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) < min(y):
        if max(x) < X and min(y) > Y:
            print('War')
        else:
            print('No War')
    else:
        print('War')

=======
Suggestion 5

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    x.sort()
    y.sort()

    if x[-1] < y[0] and x[-1] < Y and y[0] > X:
        print('No War')
    else:
        print('War')

=======
Suggestion 6

def main():
    N, M, X, Y = map(int, input().split())
    x_list = [int(x) for x in input().split()]
    y_list = [int(y) for y in input().split()]
    max_x = max(x_list)
    min_y = min(y_list)
    if max_x < min_y:
        if X < max_x < Y:
            if X < min_y <= Y:
                print("No War")
            else:
                print("War")
        else:
            print("War")
    else:
        print("War")

=======
Suggestion 7

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # print(N, M, X, Y)
    # print(x)
    # print(y)
    x_max = max(x)
    y_min = min(y)
    # print(x_max)
    # print(y_min)
    for z in range(X+1, Y+1):
        # print(z)
        if x_max < z <= y_min:
            print('No War')
            break
    else:
        print('War')

=======
Suggestion 8

def main():
    n, m, x, y = map(int, input().split())
    xa = set(map(int, input().split()))
    ya = set(map(int, input().split()))
    for z in range(x+1, y+1):
        if z not in xa and z not in ya:
            print('No War')
            exit()
    print('War')

=======
Suggestion 9

def main():
    #input
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    #compute
    if max(x) < min(y) and max(x) < Y and X < min(y):
        ans = "No War"
    else:
        ans = "War"
    #output
    print(ans)
