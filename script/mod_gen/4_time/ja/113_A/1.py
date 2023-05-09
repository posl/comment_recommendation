def main():
    x, y = map(int, input().split())
    if y % 2 == 0:
        print(int(x + y / 2))
    else:
        print('error')

if __name__ == '__main__':
    main()