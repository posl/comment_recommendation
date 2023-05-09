def main():
    A,B,C,D = map(int,input().split())
    if A == C and B == D:
        print("Draw")
    elif A == C:
        if B < D:
            print("Aoki")
        else:
            print("Takahashi")
    elif A < C:
        print("Aoki")
    else:
        print("Takahashi")

if __name__ == '__main__':
    main()