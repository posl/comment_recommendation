def main():
    S = input()
    if S[0].isupper() and S[-1].isupper() and len(S) == 8 and S[1:7].isdigit() and int(S[1:7]) >= 100000 and int(S[1:7]) <= 999999:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()