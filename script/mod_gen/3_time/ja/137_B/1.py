def main():
    K, X = map(int, input().split())
    for i in range(X - K + 1, X + K):
        print(i, end=" ")

if __name__ == '__main__':
    main()