def main():
    S = input()
    print("Yes" if S[0].isupper() and S[1:7].isdigit() and S[7].isupper() else "No")

if __name__ == '__main__':
    main()