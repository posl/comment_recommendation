def main():
    N = int(input())
    S = input()
    if S[0] == "0":
        print("Takahashi")
    elif S[0] == "1":
        if S.count("1") % 2 == 0:
            print("Takahashi")
        else:
            print("Aoki")

if __name__ == '__main__':
    main()