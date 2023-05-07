def main():
    n = int(input())
    s = input()
    if s.count('0')%2 == 1:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    main()