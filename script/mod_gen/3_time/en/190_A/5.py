def main():
    a, b, c = map(int, input().split())
    if a > b:
        print('Takahashi')
    elif a < b:
        print('Aoki')
    else:
        if c == 0:
            print('Aoki')
        else:
            print('Takahashi')

if __name__ == '__main__':
    main()