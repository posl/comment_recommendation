def main():
    n, d = map(int, input().split())
    print(1 + (n - 1) // (d * 2 + 1))

if __name__ == '__main__':
    main()