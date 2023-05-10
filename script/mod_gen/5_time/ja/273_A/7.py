def main():
    n = int(input())
    if n == 0:
        print(1)
    else:
        print(n*main())

if __name__ == '__main__':
    main()