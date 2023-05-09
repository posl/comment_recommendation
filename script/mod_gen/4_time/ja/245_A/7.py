def main():
    A, B, C, D = map(int, input().split())
    if A == C:
        if B == D:
            print("Takahashi")
        elif B > D:
            print("Takahashi")
        else:
            print("Aoki")
    elif A > C:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()