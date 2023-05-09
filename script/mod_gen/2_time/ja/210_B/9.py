def main():
    N = int(input())
    S = input()
    print('Aoki' if S.find('1') % 2 == 0 else 'Takahashi')

if __name__ == '__main__':
    main()