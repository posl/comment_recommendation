def main():
    # Read three integers
    a, b, c = map(int, input().split())
    # If there are two same numbers among a, b, and c, print the remaining number. Otherwise, print 0.
    if a == b:
        print(c)
    elif a == c:
        print(b)
    elif b == c:
        print(a)
    else:
        print(0)

if __name__ == '__main__':
    main()