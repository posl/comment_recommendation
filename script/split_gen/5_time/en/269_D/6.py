def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    x_min = min(X)
    x_max = max(X)
    y_min = min(Y)
    y_max = max(Y)
    x_range = x_max - x_min
    y_range = y_max - y_min
    x_range += 1
    y_range += 1
    if x_range > y_range:
        x_range, y_range = y_range, x_range
    if x_range == 1:
        print(1)
        exit()
    elif x_range == 2:
        print(2)
        exit()
    elif x_range == 3:
        if y_range == 3:
            print(2)
            exit()
        else:
            print(3)
            exit()
    elif x_range == 4:
        if y_range == 4:
            print(3)
            exit()
        else:
            print(4)
            exit()
    else:
        print(4)
        exit()
