def main():
    K, X = map(int, input().split())
    if K == 1:
        print(X)
    else:
        print(" ".join(map(str, range(X - K + 1, X + K))))

if __name__ == '__main__':
    main()