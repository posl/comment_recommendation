def main():
    R, C = map(int, input().split())
    if R % 2 == 0 and C % 2 == 0:
        print('black')
    elif R % 2 == 0 and C % 2 != 0:
        print('white')
    elif R % 2 != 0 and C % 2 == 0:
        print('white')
    elif R % 2 != 0 and C % 2 != 0:
        print('black')

if __name__ == '__main__':
    main()