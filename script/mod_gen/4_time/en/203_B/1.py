def main():
    n, k = map(int, input().split())
    print( (n * (n + 1) // 2) * 100 * k + (k * (k + 1) // 2) * n)

if __name__ == '__main__':
    main()