def main():
    a, b = map(int, input().split())
    if a == 1 and b == 2 or a == 2 and b == 1:
        print('Yes')
    elif a == 2 and b == 3 or a == 3 and b == 2:
        print('Yes')
    elif a == 3 and b == 4 or a == 4 and b == 3:
        print('Yes')
    elif a == 4 and b == 5 or a == 5 and b == 4:
        print('Yes')
    elif a == 5 and b == 6 or a == 6 and b == 5:
        print('Yes')
    elif a == 6 and b == 7 or a == 7 and b == 6:
        print('Yes')
    elif a == 7 and b == 8 or a == 8 and b == 7:
        print('Yes')
    elif a == 8 and b == 9 or a == 9 and b == 8:
        print('Yes')
    elif a == 9 and b == 10 or a == 10 and b == 9:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()