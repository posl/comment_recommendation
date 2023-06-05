def main():
    K, X = map(int, input().split())
    start = X - K + 1
    end = X + K
    for i in range(start, end):
        print(i, end=" ")

if __name__ == '__main__':
    main()