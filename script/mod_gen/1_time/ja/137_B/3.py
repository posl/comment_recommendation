def main():
    K, X = map(int, input().split())
    print(" ".join(map(str, range(X - K + 1, X + K))))

if __name__ == '__main__':
    main()