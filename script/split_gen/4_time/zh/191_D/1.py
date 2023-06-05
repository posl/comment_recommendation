def main():
    # input
    X, Y, R = map(float, input().split())
    # compute
    X_min = int(X - R)
    X_max = int(X + R)
    Y_min = int(Y - R)
    Y_max = int(Y + R)
    count = 0
    for x in range(X_min, X_max + 1):
        for y in range(Y_min, Y_max + 1):
            if (X - x) ** 2 + (Y - y) ** 2 <= R ** 2:
                count += 1
    # output
    print(count)
