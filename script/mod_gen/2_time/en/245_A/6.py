def main():
    a,b,c,d = map(int, input().split())
    if a < c:
        print('Aoki')
    elif c < a:
        print('Takahashi')
    else:
        if b < d:
            print('Aoki')
        else:
            print('Takahashi')

if __name__ == '__main__':
    main()