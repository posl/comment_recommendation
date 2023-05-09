def main():
    S = input()
    if S[0].isupper() and S[7].isupper() and S[1:7].isdigit() and 100000 <= int(S[1:7]) <= 999999:
        print("Yes")
    else:
        print("No")
main()

if __name__ == '__main__':
    main()