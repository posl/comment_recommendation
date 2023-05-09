Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.append(X)
    y.append(Y)
    if max(x) < min(y):
        print('No War')
    else:
        print('War')

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
    x_max = max(x)
    y_min = min(y)
    if x_max < y_min and X < y_min and y_min <= Y:
        print("No War")
    else:
        print("War")

main()

=======
Suggestion 4

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) < min(y) and X < min(y) and max(x) < Y:
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
    if X < min(y) and max(x) < Y and max(x) < min(y):
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
    if x[-1] < y[0] and X < y[0] and y[0] <= Y:
        print('No War')
    else:
        print('War')

=======
Suggestion 7

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if X < min(y) and max(x) < Y and max(x) < min(y):
        print("No War")
    else:
        print("War")

=======
Suggestion 8

def main():
    n, m, x, y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    if max(x) < min(y) and x < y:
        print("No War")
    else:
        print("War")

=======
Suggestion 9

def war_or_no_war(N, M, X, Y, x, y):
    # x_max = max(x)
    # y_min = min(y)
    # if x_max < y_min:
    #     return "No War"
    # else:
    #     return "War"
    if max(x) < min(y) and X < min(y) and min(y) <= Y:
        return "No War"
    else:
        return "War"
