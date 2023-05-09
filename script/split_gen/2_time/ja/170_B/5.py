def main():
    X, Y = map(int, input().split())
    if 4 * X - Y >= 0 and 4 * X - Y <= 4 * X and Y % 2 == 0:
        print('Yes')
    else:
        print('No')
