def main():
    a, b = map(int, input().split())
    if (a * b * 3) % 2 == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()