Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.append(X)
    y.append(Y)
    if max(x) < min(y):
        print("No War")
    else:
        print("War")

=======

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    if max(x) < min(y) and max(x) < Y and max(y) > X:
        print("No War")
    else:
        print("War")

=======

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    if max(x) < min(y) and max(x) < Y and min(y) > X:
        print("No War")
    else:
        print("War")

=======

def main():
    N, M, X, Y = map(int, input().split())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    x_max = max(x_list)
    y_min = min(y_list)
    if x_max < y_min and X < y_min and x_max < Y:
        print("No War")
    else:
        print("War")

=======

def solve():
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

def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if (max(x) < min(y)) and (max(x) < Y) and (min(y) > X):
        print("No War")
    else:
        print("War")

=======

def main():
    N, M, X, Y = list(map(int, input().split()))
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if max(x) < min(y) and max(x) < Y and max(y) > X:
        print("No War")
    else:
        print("War")

main()

=======

def main():
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.append(x)
    b.append(y)
    a.sort()
    b.sort()

    print("No War" if a[-1] < b[0] else "War")

=======

def war(N, M, X, Y, x, y):
    if X >= Y: return "War"
    if max(x) >= min(y): return "War"
    if max(x) >= Y: return "War"
    if min(y) <= X: return "War"
    return "No War"

N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(war(N, M, X, Y, x, y))
