def main():
    N, K, A = map(int, input().split())
    if N == A:
        print(K % N)
    else:
        if K % N >= A:
            print(A + K % N - 1)
        else:
            print(K % N)

if __name__ == '__main__':
    main()