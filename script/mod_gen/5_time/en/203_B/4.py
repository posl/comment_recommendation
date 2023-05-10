def main():
    N, K = map(int, input().split())
    print(int((N * (N + 1) * K * (K + 1)) / 4))

if __name__ == '__main__':
    main()