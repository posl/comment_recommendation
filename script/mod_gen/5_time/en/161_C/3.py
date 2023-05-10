def main():
    n, k = map(int, input().split())
    print(min(n % k, abs(n % k - k)))

if __name__ == '__main__':
    main()