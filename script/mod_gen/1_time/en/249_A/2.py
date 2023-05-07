def main():
    A, B, C, D, E, F, X = map(int, input().split())
    takahashi = (A + C) * B
    aoki = (D + F) * E
    if takahashi > aoki:
        print("Takahashi")
    elif aoki > takahashi:
        print("Aoki")
    else:
        print("Draw")

if __name__ == '__main__':
    main()