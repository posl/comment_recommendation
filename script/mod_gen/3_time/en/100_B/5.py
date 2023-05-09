def main():
    d, n = map(int, input().split())
    if n == 100:
        n += 1
    print(n * (100 ** d))

if __name__ == '__main__':
    main()