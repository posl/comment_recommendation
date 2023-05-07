def main():
    A,B,C,D,E,F,X = map(int, input().split())
    Takahashi = 0
    Aoki = 0
    for i in range(0,X):
        if i < A:
            Takahashi += B
        elif i >= A and i < A + C:
            Takahashi += 0
        elif i >= A + C:
            Takahashi += B
    for j in range(0,X):
        if j < D:
            Aoki += E
        elif j >= D and j < D + F:
            Aoki += 0
        elif j >= D + F:
            Aoki += E
    if Takahashi > Aoki:
        print("Takahashi")
    elif Takahashi < Aoki:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()