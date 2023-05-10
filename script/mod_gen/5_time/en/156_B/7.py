def main():
    n, k = map(int, input().split())
    digit = 0
    while n >= k:
        n = n // k
        digit += 1
    print(digit + 1)

if __name__ == '__main__':
    main()