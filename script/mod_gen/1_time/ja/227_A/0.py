def main():
    N, K, A = map(int, input().split())
    print(K % N + A - 1 if K % N + A - 1 <= N else K % N + A - 1 - N)

if __name__ == '__main__':
    main()