def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    if k == 1:
        print(1)
        return
    n = 1
    while True:
        if (10 ** n - 1) % k == 0:
            print(n)
            return
        n += 1

if __name__ == '__main__':
    main()