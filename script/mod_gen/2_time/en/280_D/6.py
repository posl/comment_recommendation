def main():
    k = int(input())
    n = 1
    while True:
        if (n * (n + 1)) % k == 0:
            print(n + 1)
            break
        n += 1

if __name__ == '__main__':
    main()