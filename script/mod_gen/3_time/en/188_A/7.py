def main():
    # Read the input
    X, Y = map(int, input().split())
    # Check if the team which is behind can turn the tables
    if abs(X - Y) < 3:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()