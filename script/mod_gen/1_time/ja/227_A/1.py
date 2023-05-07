def main():
    N, K, A = map(int, input().split())
    if K % N == 0:
        print(A)
    else:
        print((A + K % N - 1) % N + 1)

if __name__ == '__main__':
    main()