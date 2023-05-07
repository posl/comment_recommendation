def main():
    X, Y, A, B = map(int, input().split())
    exp = 0
    while Y > X * A and X * (A - 1) + B >= B:
        X *= A
        exp += 1
    exp += (Y - X - 1) // B
    print(exp)

if __name__ == '__main__':
    main()