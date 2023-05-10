def main():
    n, a, b = map(int, input().split())
    if n == 1:
        if a > 0:
            print(1)
        else:
            print(0)
    else:
        if a == 0:
            print(0)
        else:
            if b == 0:
                print(1)
            else:
                if a > b:
                    print(1)
                else:
                    print((n-1)*a+b)

if __name__ == '__main__':
    main()