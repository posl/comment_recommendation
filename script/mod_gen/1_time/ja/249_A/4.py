def main():
    A, B, C, D, E, F, X = map(int, input().split())
    T = A * B * X // (A * B + C * (X // (A + C)))
    A = X - T
    T = A * B
    A = X - T // (D + E) * D
    T = A * E
    if T > T:
        print("Takahashi")
    elif T < T:
        print("Aoki")
    else:
        print("Draw")
main()

if __name__ == '__main__':
    main()