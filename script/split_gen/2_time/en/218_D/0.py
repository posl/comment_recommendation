def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X.sort()
    Y.sort()
    x_count = {}
    y_count = {}
    for i in range(N):
        if X[i] in x_count:
            x_count[X[i]] += 1
        else:
            x_count[X[i]] = 1
        if Y[i] in y_count:
            y_count[Y[i]] += 1
        else:
            y_count[Y[i]] = 1
    x_sum = 0
    y_sum = 0
    for i in range(N):
        x_sum += x_count[X[i]] - 1
        y_sum += y_count[Y[i]] - 1
    print(x_sum * y_sum)
