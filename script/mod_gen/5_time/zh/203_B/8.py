def main():
    n, k = map(int, input().split())
    print(n * (n + 1) * k * 100 // 2)

if __name__ == '__main__':
    main()