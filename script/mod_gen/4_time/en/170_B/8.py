def main():
    x, y = map(int, input().split())
    if x == 2:
        if y == 2 or y == 4:
            print('Yes')
        else:
            print('No')
    elif x == 4:
        if y == 2 or y == 4 or y == 6 or y == 8:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

if __name__ == '__main__':
    main()