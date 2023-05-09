def main():
    R, C = map(int, input().split())
    if R % 2 == 1:
        if C % 2 == 1:
            print('black')
        else:
            print('white')
    else:
        if C % 2 == 1:
            print('white')
        else:
            print('black')

if __name__ == '__main__':
    main()