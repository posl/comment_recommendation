def main():
    K, X = map(int, input().split())
    for i in range(-K + 1, K):
        print(X + i, end=' ')
main()

if __name__ == '__main__':
    main()