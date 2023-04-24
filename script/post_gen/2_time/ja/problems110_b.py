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
    if x[len(x) - 1] < y[0]:
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
        print("No War")
    else:
        print("War")

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
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_list.append(X)
    y_list.append(Y)
    x_list.sort()
    y_list.sort()
    if x_list[-1] < y_list[0]:
        print("No War")
    else:
        print("War")

=======
Suggestion 5

def main():
    # 入力
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    # 処理
    Z = max(x) + 1
    if Z <= Y and Z > X:
        for i in range(M):
            if Z <= y[i]:
                print("War")
                break
        else:
            print("No War")
    else:
        print("War")

=======
Suggestion 6

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.sort()
    y.sort()
    if x[-1] < y[0] and X < y[0] <= Y:
        print('No War')
    else:
        print('War')

=======
Suggestion 7

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.sort()
    y.sort()
    if X < y[0] <= Y and x[-1] < y[0]:
        print("No War")
    else:
        print("War")

=======
Suggestion 8

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    Z = max(x) + 1
    if Z <= Y and Z > X:
        print('No War')
    else:
        print('War')

=======
Suggestion 9

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    z = max(x) + 1
    if z > min(y) or z <= X or z > Y:
        print('War')
    else:
        print('No War')

=======
Suggestion 10

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    z = X+1
    while z<=Y:
        if z not in x and z not in y:
            print("No War")
            return
        z += 1
    print("War")
    return
