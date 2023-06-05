def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x.append(int(input()))
        y.append(int(input()))
    x.sort()
    y.sort()
    x_diff = []
    y_diff = []
    for i in range(n - 1):
        x_diff.append(x[i + 1] - x[i])
        y_diff.append(y[i + 1] - y[i])
    x_diff.sort()
    y_diff.sort()
    print(max(x_diff[-1], y_diff[-1]))
