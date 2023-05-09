def main():
    A, B, C, D = map(int, input().split())
    if A > C:
        print("Takahashi")
    elif A < C:
        print("Aoki")
    elif A == C:
        if B > D:
            print("Takahashi")
        elif B < D:
            print("Aoki")
        elif B == D:
            print("same")

if __name__ == '__main__':
    main()