def main():
    A,B,C = map(int,input().split())
    if C == 0 and A > B:
        print("Takahashi")
    elif C == 1 and A >= B:
        print("Takahashi")
    else:
        print("Aoki")

if __name__ == '__main__':
    main()