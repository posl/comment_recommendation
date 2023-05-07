def main():
    a, b, c, d, e, f, x = map(int, input().split())
    takahashi = (a + c) * (x // (a + c)) + b * (x % (a + c) // a)
    aoki = (d + f) * (x // (d + f)) + e * (x % (d + f) // d)
    if takahashi > aoki:
        print('Takahashi')
    elif takahashi < aoki:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()