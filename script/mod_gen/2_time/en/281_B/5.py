def main():
    S = input()
    if S[0].isupper() and S[-1].isupper() and S[1:7].isdigit() and S[1:7].isdecimal() and int(S[1:7]) in range(100000, 999999+1):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()