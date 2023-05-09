def main():
    k = int(input())
    n = 1
    while True:
        if n % 2 == 0 or n % 5 == 0:
            n += 1
            continue
        if k % n == 0:
            print(n)
            break
        n += 1

if __name__ == '__main__':
    main()