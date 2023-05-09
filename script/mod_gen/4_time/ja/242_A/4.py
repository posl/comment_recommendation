def main():
    a, b, c, x = map(int, input().split())
    if x >= a:
        if x <= b:
            print(c / (b - a + 1))
        else:
            print(0)
    else:
        print(0)

if __name__ == '__main__':
    main()