def main():
    K, X = map(int, input().split())
    print(*[X - K + 1 + i for i in range(2 * K - 1)])

if __name__ == '__main__':
    main()