def main():
    X, K = map(int, input().split())
    d = 10**K
    print((X + d // 2) // d * d)

if __name__ == '__main__':
    main()