def main():
    X, Y = map(int, input().split())
    if Y % 2 == 0:
        if 2 * X <= Y and 4 * X >= Y:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
