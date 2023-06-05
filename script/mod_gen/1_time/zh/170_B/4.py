def main():
    x, y = map(int, input().split())
    if x == y == 2:
        print('Yes')
    elif x * 2 <= y <= x * 4 and y % 2 == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()