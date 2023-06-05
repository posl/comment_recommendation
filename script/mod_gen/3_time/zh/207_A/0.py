def main():
    a, b, c = map(int, input().split())
    if a > b:
        if a > c:
            print(a + max(b, c))
        else:
            print(c + b)
    else:
        if b > c:
            print(b + max(a, c))
        else:
            print(a + c)

if __name__ == '__main__':
    main()