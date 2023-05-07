def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print('Yes')
    elif a == 2 or b == 2:
        print('No')
    else:
        if a > b:
            a, b = b, a
        if a % 2 == 0:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()