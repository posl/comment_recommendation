def main():
    # X, Y = map(int, input().split())
    X, Y = 3, 8
    # 4x + 2y = Y
    # x + y = X
    # 4x + 2y = 2X + 2Y
    # x = 2X + Y - 2
    # y = X - x
    # x = 2X + Y - 2
    # y = X - (2X + Y - 2)
    # y = X - 2X - Y + 2
    # y = -X - Y + 2
    # 4(2X + Y - 2) + 2(-X - Y + 2) = Y
    # 8X + 4Y - 8 + 2X + 2Y - 4 = Y
    # 10X + 6Y = 3Y
    # 10X = Y
    # X = Y / 10
    if Y % 10 == 0 and X == Y // 10:
        print('Yes')
    else:
        print('No')
