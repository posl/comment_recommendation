def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        exit()
    n = 1
    while True:
        if (n * (n + 1) // 2) % k == 0:
            print(n + 1)
            exit()
        n += 1

if __name__ == '__main__':
    main()