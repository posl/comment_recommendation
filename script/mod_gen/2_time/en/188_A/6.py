def main():
    X, Y = map(int, input().strip().split())
    if X > Y:
        if X - Y >= 3:
            print('No')
        else:
            print('Yes')
    elif Y > X:
        if Y - X >= 3:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()