def main():
    N, K, A = map(int, input().split())
    if K > N:
        K = K % N
    if (A + K) > N:
        print(K - (N - A))
    else:
        print(A + K)

if __name__ == '__main__':
    main()