def main():
    a, b = map(int, input().split())
    if a == 1:
        if b == 1:
            print('No')
        else:
            print('Yes')
    elif a == 2:
        if b == 2:
            print('No')
        else:
            print('Yes')
    else:
        if b == 3:
            print('No')
        else:
            print('Yes')

if __name__ == '__main__':
    main()