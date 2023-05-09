def main():
    X, Y = map(int, input().split())
    if Y % 2 == 0 and Y // 2 >= X and 4 * X >= Y:
        print('Yes')
    else:
        print('No')
main()

if __name__ == '__main__':
    main()