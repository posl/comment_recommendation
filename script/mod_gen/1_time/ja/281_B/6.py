def main():
    S = input()
    if len(S) < 3:
        print("No")
        exit()
    if S[0].isupper() and S[-1].isupper():
        for i in range(1, len(S)-1):
            if not S[i].isnumeric():
                print("No")
                exit()
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()