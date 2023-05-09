def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while X < Y:
        if X * A < X + B:
            X *= A
            exp += 1
        else:
            break
    exp += (Y - 1 - X) // B
    print(exp)

if __name__ == '__main__':
    main()