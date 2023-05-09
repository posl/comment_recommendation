def main():
    A, B, C, D, E, F, X = map(int, input().split())
    Takahashi = 0
    Aoki = 0
    for i in range(1, X+1):
        if i % (A + B) <= A:
            Takahashi += 1
        if i % (D + E) <= D:
            Aoki += 1
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()