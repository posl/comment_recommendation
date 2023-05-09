def main():
    # Take input
    A, B, C, D = map(int, input().split())
    # Logic goes here
    if (A > C):
        print("Takahashi")
    elif (A == C):
        if (B > D):
            print("Takahashi")
        elif (B < D):
            print("Aoki")
        else:
            print("Same")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()