def main():
    N, D = map(int, input().split())
    print(int(N / (2 * D + 1)) + (1 if N % (2 * D + 1) else 0))

if __name__ == '__main__':
    main()