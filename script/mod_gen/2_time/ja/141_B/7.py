def main():
    S = input()
    if S[::2] == 'RUDL' and S[1::2] == 'LUDR':
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()