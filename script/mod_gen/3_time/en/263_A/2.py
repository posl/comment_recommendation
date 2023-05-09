def main():
    a, b, c, d, e = map(int, input().split())
    if (a == b and b == c and d == e and a != d) or (a == b and c == d and d == e and a != c):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()