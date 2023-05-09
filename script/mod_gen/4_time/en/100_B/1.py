def main():
    d,n = map(int,input().split())
    if n == 100:
        if d == 0:
            print(101)
        elif d == 1:
            print(10100)
        elif d == 2:
            print(1010000)
    else:
        if d == 0:
            print(n)
        elif d == 1:
            print(n*100)
        elif d == 2:
            print(n*10000)

if __name__ == '__main__':
    main()