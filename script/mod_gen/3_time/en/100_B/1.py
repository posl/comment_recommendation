def main():
    d, n = map(int, input().split())
    if d == 0:
        print(n)
    elif d == 1:
        if n == 100:
            print(10100)
        else:
            print(n*100)
    else:
        if n == 100:
            print(1010000)
        else:
            print(n*10000)

if __name__ == '__main__':
    main()