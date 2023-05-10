def main():
    x,y = map(int, input().split())
    if y % 2 == 0 and y >= 2 * x and y <= 4 * x:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()