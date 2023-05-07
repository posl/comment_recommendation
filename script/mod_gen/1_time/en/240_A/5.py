def main():
    a, b = map(int, input().split())
    if 1 <= a < b <= 10:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()