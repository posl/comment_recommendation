def main():
    a, b, c = map(int, input().split())
    if a == b and a != c:
        print('Yes')
    elif a == c and a != b:
        print('Yes')
    elif b == c and b != a:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()