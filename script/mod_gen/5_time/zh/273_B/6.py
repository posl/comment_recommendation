def main():
    x, k = map(int, input().split())
    for i in range(k):
        if x % (10 ** (i + 1)) <= 5 * 10 ** i:
            print(x - x % (10 ** (i + 1)))
            return
    print(10 ** k)

if __name__ == '__main__':
    main()