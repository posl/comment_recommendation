def main():
    a, b = map(int, input().split())
    if a == 1 or a == 3 or a == 6 or a == 8 or a == 10:
        if b == a + 1:
            print('Yes')
        else:
            print('No')
    elif a == 2 or a == 4 or a == 5 or a == 7 or a == 9:
        if b == a + 1 or b == a + 3:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()