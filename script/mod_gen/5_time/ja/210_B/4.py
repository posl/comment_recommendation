def main():
    N = int(input())
    S = input()
    if S.count('1') % 2 == 1:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    main()