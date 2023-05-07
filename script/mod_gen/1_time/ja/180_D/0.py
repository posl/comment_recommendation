def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while True:
        if X * A < X + B and X * A < Y:
            X *= A
            exp += 1
        elif X + B < Y:
            X += B
            exp += 1
        else:
            break
    print(exp)

if __name__ == '__main__':
    main()