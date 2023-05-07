def main():
    N = int(input())
    S = input()
    if S[0] == '0':
        print('Takahashi')
    else:
        if N % 2 == 1:
            print('Aoki')
        else:
            print('Takahashi')
main()

if __name__ == '__main__':
    main()