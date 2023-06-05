def main():
    n = int(input())
    s = input()
    if s.count('1') % 2 == 0:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    main()