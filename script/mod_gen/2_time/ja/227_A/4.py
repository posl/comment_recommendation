def main():
    N, K, A = map(int, input().split())
    print((A-1 + K) % N + 1)

if __name__ == '__main__':
    main()