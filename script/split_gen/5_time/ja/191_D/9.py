def main():
    X, Y, R = map(float, input().split())
    count = 0
    for x in range(int(X - R) - 1, int(X + R) + 1):
        for y in range(int(Y - R) - 1, int(Y + R) + 1):
            if (x - X) ** 2 + (y - Y) ** 2 <= R ** 2:
                count += 1
    print(count)
