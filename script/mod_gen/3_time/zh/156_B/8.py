def main():
    n, k = map(int, input().split())
    count = 0
    while n > 0:
        count += 1
        n //= k
    print(count)

if __name__ == '__main__':
    main()