def main():
    a, b = map(int, input().split())
    if a + 1 == b:
        print('Yes')
    elif a == 15 and b == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()