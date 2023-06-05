def main():
    N, K = map(int, input().split())
    print(sum([i * 100 + j for i in range(1, N + 1) for j in range(1, K + 1)]))

if __name__ == '__main__':
    main()