def main():
    n, m = map(int, input().split())
    if n == 0 or m == 0:
        print(0)
    elif n == 1 and m == 1:
        print(0)
    else:
        print(n * m - 1)

if __name__ == '__main__':
    main()