def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while True:
        if A * X >= Y:
            break
        if A * X < X + B:
            break
        X *= A
        exp += 1
    exp += (Y - X - 1) // B
    print(exp)

if __name__ == '__main__':
    main()