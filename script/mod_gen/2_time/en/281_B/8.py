def main():
    S = input()
    if len(S) == 10 and S[0].isupper() and S[1:7].isdigit() and S[7].isupper():
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()