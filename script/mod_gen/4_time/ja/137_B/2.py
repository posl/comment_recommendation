def main():
    K, X = map(int, input().split())
    print(*[x for x in range(X - K + 1, X + K)])

if __name__ == '__main__':
    main()