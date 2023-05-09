def main():
    K, X = map(int, input().split())
    print("Yes" if K * 500 >= X else "No")

if __name__ == '__main__':
    main()