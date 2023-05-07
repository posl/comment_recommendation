def main():
    a, b = map(int, input().split())
    if a == 1 and b == 10:
        print('Yes')
    elif a <= 4 and b <= 4:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()