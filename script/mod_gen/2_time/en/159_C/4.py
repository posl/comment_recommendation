def main():
    L = int(input())
    a = L / 3
    b = L / 3
    c = L / 3
    if a % 1 == 0:
        a -= 1
        b -= 1
        c -= 1
    if a % 2 == 0:
        a /= 2
        b /= 2
    if b % 2 == 0:
        b /= 2
        c /= 2
    if c % 2 == 0:
        c /= 2
        a /= 2
    print(a * b * c)

if __name__ == '__main__':
    main()