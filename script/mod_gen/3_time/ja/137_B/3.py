def main():
    K, X = map(int, input().split())
    ans = [i for i in range(X - K + 1, X + K)]
    print(*ans)

if __name__ == '__main__':
    main()