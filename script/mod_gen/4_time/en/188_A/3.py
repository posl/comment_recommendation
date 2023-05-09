def main():
    x, y = map(int, input().split())
    if x < y:
        if x + 3 > y:
            print('Yes')
            return
    else:
        if y + 3 > x:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    main()