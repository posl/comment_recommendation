def main():
    A, B, C = map(int, input().split())
    if C == 0:
        if A > B:
            print("Takahashi")
        else:
            print("Aoki")
    elif C == 1:
        if B > A:
            print("Aoki")
        else:

if __name__ == '__main__':
    main()