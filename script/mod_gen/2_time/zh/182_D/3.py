def main():
    n = input()
    k = len(n)
    n = int(n)
    if n % 3 == 0:
        print(0)
        return
    for i in range(k):
        for j in range(1, k):
            if i + j > k:
                break
            if n % 3 == 0:
                print(i)
                return
            n1 = n // (10 ** (k - i - j))
            n2 = n % (10 ** (k - i - j - 1))
            n = n1 * (10 ** (k - i - j - 1)) + n2
    print(-1)

if __name__ == '__main__':
    main()