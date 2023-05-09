def main():
    n = int(input())
    s = input()
    print('Takahashi' if s.find('1') % 2 == 0 else 'Aoki')

if __name__ == '__main__':
    main()