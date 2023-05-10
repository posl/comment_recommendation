def main():
    x, y = map(int, input().split())
    if y % 2 == 0 and (y - x * 2) % 2 == 0 and (y - x * 2) / 2 >= 0 and x - (y - x * 2) / 2 >= 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()