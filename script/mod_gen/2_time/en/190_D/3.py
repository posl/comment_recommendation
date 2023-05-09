def main():
    N = int(input())
    i = 1
    count = 0
    while i * i <= 2 * N:
        if (2 * N) % i == 0:
            if (i + (2 * N) // i - 1) % 2 == 0:
                count += 1
        i += 1
    print(count)

if __name__ == '__main__':
    main()