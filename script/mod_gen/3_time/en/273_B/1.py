def main():
    x, k = map(int, input().split())
    print((x + 5 * 10 ** (k - 1)) // 10 ** k * 10 ** k)

if __name__ == '__main__':
    main()