def main():
    A, B, C = map(int, input().split())
    if A == B:
        if C == 0:
            print("Aoki")
        else:
            print("Takahashi")
    elif A > B:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()