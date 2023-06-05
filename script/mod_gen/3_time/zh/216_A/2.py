def main():
    x, y = map(float, input().split('.'))
    if y <= 2:
        print(int(x), end='')
        print('-')
    elif y <= 6:
        print(int(x), end='')
    else:
        print(int(x), end='')
        print('+')

if __name__ == '__main__':
    main()