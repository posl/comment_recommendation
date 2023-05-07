def main():
    X, Y = map(int, input().split())
    if abs(X - Y) > 2:
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()