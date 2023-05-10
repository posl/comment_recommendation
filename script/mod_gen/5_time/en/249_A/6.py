def main():
    A,B,C,D,E,F,X = map(int, input().split())
    Takahashi = A * B
    Aoki = D * E
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()