def main():
    N = int(input())
    if N % 4 == 0:
        print('Yes')
    elif N % 7 == 0:
        print('Yes')
    elif N % 11 == 0:
        print('Yes')
    elif N % 4 == 3:
        print('Yes')
    elif N % 7 == 3:
        print('Yes')
    elif N % 11 == 3:
        print('Yes')
    elif N % 4 == 7:
        print('Yes')
    elif N % 7 == 7:
        print('Yes')
    elif N % 11 == 7:
        print('Yes')
    elif N % 4 == 11:
        print('Yes')
    elif N % 7 == 11:
        print('Yes')
    elif N % 11 == 11:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()