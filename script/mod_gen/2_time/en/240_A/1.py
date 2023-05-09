def main():
    a, b = map(int, input().split())
    if a + 1 == b or a - 1 == b or a == 1 and b == 10 or a == 10 and b == 1:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()