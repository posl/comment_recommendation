def main():
    a, b, c, d, e, f, x = map(int, input().split())
    takahashi = (a + b) * (x // (a + c)) + a * (x % (a + c) // (a + c))
    aoki = (d + e) * (x // (d + f)) + d * (x % (d + f) // (d + f))
    if takahashi < aoki:
        print('Aoki')
    elif takahashi > aoki:
        print('Takahashi')
    else:
        print('Draw')

if __name__ == '__main__':
    main()