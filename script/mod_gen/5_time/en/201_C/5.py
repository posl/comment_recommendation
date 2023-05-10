def main():
    s = input()
    o = s.count("o")
    x = s.count("x")
    q = s.count("?")
    if o >= 5:
        print(0)
    elif o == 4:
        print(24)
    elif o == 3:
        print(36)
    elif o == 2:
        print(14 + 12 * q)
    elif o == 1:
        print(1 + 4 * q + 6 * q * (q - 1))
    elif o == 0:
        print(q * (q - 1) * (q - 2) * (q - 3))
    else:
        print(0)

if __name__ == '__main__':
    main()