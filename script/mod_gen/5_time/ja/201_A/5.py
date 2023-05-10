def main():
    a, b, c = map(int, input().split())
    if a - b == b - c:
        print('Yes')
    elif a - c == c - b:
        print('Yes')
    elif b - a == a - c:
        print('Yes')
    elif b - c == c - a:
        print('Yes')
    elif c - a == a - b:
        print('Yes')
    elif c - b == b - a:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()