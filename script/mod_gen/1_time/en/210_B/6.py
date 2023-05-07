def main():
    N = int(input())
    S = input()
    if S[0] == '0':
        if S.count('1') % 2 == 0:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        print('Aoki')

if __name__ == '__main__':
    main()