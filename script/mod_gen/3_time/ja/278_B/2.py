def main():
    h, m = map(int, input().split())
    h1 = h // 10
    h2 = h % 10
    m1 = m // 10
    m2 = m % 10
    if h1 == 0 and m1 == 0:
        print(h2, m2)
    elif h1 == 0:
        if m1 <= 2 and m2 <= 3:
            print(m1, m2)
        else:
            print(h2, m2)
    elif m1 == 0:
        if h1 <= 2 and h2 <= 3:
            print(h1, h2)
        else:
            print(h2, m2)
    else:
        if h1 <= 2 and h2 <= 3 and m1 <= 2 and m2 <= 3:
            print(h1, h2)
        else:
            print(h2, m2)

if __name__ == '__main__':
    main()