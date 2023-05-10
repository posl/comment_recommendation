def main():
    X, Y = map(int, input().split())
    if Y % 2 == 0:
        if (Y/2) >= X and X >= (Y/4):
            print('Yes')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()