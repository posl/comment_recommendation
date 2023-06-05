def main():
    a, b = map(int, input().split())
    if a == 0:
        print('0 1')
    elif b == 0:
        print('1 0')
    else:
        x = a / (a + b)
        y = b / (a + b)
        print(x, y)

if __name__ == '__main__':
    main()