def main():
    a, b, c, d, e = map(int, input().split())
    if a == b and a == c and d == e:
        print('Yes')
    elif a == b and a == d and c == e:
        print('Yes')
    elif a == b and a == e and c == d:
        print('Yes')
    elif a == c and a == d and b == e:
        print('Yes')
    elif a == c and a == e and b == d:
        print('Yes')
    elif a == d and a == e and b == c:
        print('Yes')
    elif b == c and b == d and a == e:
        print('Yes')
    elif b == c and b == e and a == d:
        print('Yes')
    elif b == d and b == e and a == c:
        print('Yes')
    elif c == d and c == e and a == b:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()