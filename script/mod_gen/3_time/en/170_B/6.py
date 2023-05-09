def main():
    x, y = map(int, input().split())
    if x == 1 and y == 2:
        print('Yes')
        return
    if y % 2 == 0:
        if x * 2 == y:
            print('Yes')
            return
        elif x * 4 == y:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()