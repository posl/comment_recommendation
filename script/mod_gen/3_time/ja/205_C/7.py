def main():
    a, b, c = map(int, input().split())
    if c % 2 == 0:
        aa = abs(a)
        bb = abs(b)
        if aa == bb:
            print("=")
        elif aa > bb:
            print(">")
        else:
            print("<")
    else:
        if a == b:
            print("=")
        elif a > b:
            print(">")
        else:
            print("<")

if __name__ == '__main__':
    main()