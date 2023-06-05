def main():
    n = int(input())
    if n % 7 == 0 or n % 4 == 0:
        print('Yes')
    elif n % 11 == 0:
        print('Yes')
    else:
        print('No')
    return 0

if __name__ == '__main__':
    main()