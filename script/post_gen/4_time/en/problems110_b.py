Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) < min(y) and max(x) < Y and max(y) > X:
        print("No War")
    else:
        print("War")

main()

=======
Suggestion 2

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) < min(y) and max(x) < Y and max(y) > X:
        print("No War")
    else:
        print("War")

=======
Suggestion 3

def main():
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.append(x)
    b.append(y)
    a.sort()
    b.sort()
    if a[-1] < b[0]:
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
    z = x_max + 1

    if z > y_min:
        print('War')
    elif z <= X or z > Y:
        print('War')
    else:
        print('No War')

=======
Suggestion 5

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) >= min(y) or max(x) >= Y or min(y) <= X:
        print('War')
    else:
        print('No War')

=======
Suggestion 6

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.sort()
    y.sort()
    if x[-1] < y[0] and X < y[0] and x[-1] < Y:
        print("No War")
    else:
        print("War")

=======
Suggestion 7

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.sort(reverse=True)
    y.sort()
    for i in range(101):
        if x[0] < i <= y[0] and X < i <= Y:
            print('No War')
            return
    print('War')

=======
Suggestion 8

def main():
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if max(a) < min(b) and max(a) < y and min(b) > x:
        print('No War')
    else:
        print('War')

=======
Suggestion 9

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if (max(x) < min(y)) and (max(x) < Y) and (X < min(y)):
        print("No War")
    else:
        print("War")

=======
Suggestion 10

def main():
    #Read input
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    #Check if war will break out
    if max(x) < min(y) and max(x) < Y and X < min(y):
        print("No War")
    else:
        print("War")
    return
