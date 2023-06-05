def main():
    a, b = map(int, input().split())
    if b == 1:
        print(0)
    else:
        if b % a == 0:
            print(b // a)
        else:
            print(b // a + 1)

if __name__ == '__main__':
    main()