def main():
    A,B,C,D = map(int, input().split())
    if A < C:
        print("Takahashi")
    elif A > C:
        print("Aoki")
    else:
        if B < D:
            print("Takahashi")
        else:
            print("Aoki")

if __name__ == '__main__':
    main()