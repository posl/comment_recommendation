def main():
    S = input()
    if (S[::2].find('L') == -1 and S[1::2].find('R') == -1):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()