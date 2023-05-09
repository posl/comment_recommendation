def main():
    a, b, c, x = map(int, input().split())
    if x <= a:
        print(1)
    elif a < x <= a + c:
        print(1 / (b - a + 1))
    else:
        print(0)

if __name__ == '__main__':
    main()