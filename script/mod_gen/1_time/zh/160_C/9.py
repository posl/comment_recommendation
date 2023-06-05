def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    max = 0
    for i in range(N):
        if i == N-1:
            if max < K - A[i] + A[0]:
                max = K - A[i] + A[0]
        else:
            if max < A[i+1] - A[i]:
                max = A[i+1] - A[i]
    print(K-max)

if __name__ == '__main__':
    main()