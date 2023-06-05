def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print((10 ** n - 9 ** n - 9 ** n + 8 ** n) % (10 ** 9 + 7))

if __name__ == '__main__':
    main()