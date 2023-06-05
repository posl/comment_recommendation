def main():
    N, D = map(int, input().split())
    print(N // (2 * D + 1) + (N % (2 * D + 1) > 0))

if __name__ == '__main__':
    main()