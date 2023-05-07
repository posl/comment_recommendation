def main():
    K, X = map(int, input().split())
    for i in range(2 * K - 1):
        print(X - K + 1 + i)

if __name__ == '__main__':
    main()