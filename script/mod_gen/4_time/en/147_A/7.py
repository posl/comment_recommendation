def main():
    a, b, c = map(int, input().split())
    print('win' if a+b+c < 22 else 'bust')

if __name__ == '__main__':
    main()