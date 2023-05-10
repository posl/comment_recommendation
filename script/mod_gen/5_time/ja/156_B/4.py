def main():
    n, k = map(int, input().split())
    count = 0
    while True:
        n //= k
        count += 1
        if n == 0:
            break
    print(count)

if __name__ == '__main__':
    main()