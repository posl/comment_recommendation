def main():
    d, n = map(int, input().split())
    if n == 100:
        n = 101
    print(100**d * n)

if __name__ == '__main__':
    main()