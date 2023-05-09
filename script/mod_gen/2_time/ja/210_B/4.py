def main():
    N = int(input())
    S = input()
    if S[0] == '0':
        print('Takahashi')
    else:
        if S.count('0') == 0:
            print('Aoki')
        else:
            print('Takahashi')

if __name__ == '__main__':
    main()