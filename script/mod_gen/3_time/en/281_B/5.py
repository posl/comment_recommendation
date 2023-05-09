def main():
    S = input()
    if S[0] == S[-1] and S[0].isupper() and S[-1].isupper() and S[1:7].isdigit() and 100000 <= int(S[1:7]) <= 999999:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()