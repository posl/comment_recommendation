def main():
    S = input().strip()
    if S[0].isupper() and S[-1].isupper() and len(S) == 8 and S[1:-1].isdigit() and 100000 <= int(S[1:-1]) <= 999999:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()