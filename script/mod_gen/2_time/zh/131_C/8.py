def main():
    N, L = map(int, input().split())
    print(N * L + N * (N - 1) // 2)

if __name__ == '__main__':
    main()