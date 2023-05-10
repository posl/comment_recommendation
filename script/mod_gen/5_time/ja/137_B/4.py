def main():
    K, X = map(int, input().split())
    # K, X = 3, 7
    # K, X = 4, 0
    # K, X = 1, 100
    start = X - K + 1
    end = X + K
    for i in range(start, end):
        print(i, end=' ')
    print(end)

if __name__ == '__main__':
    main()