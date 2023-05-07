def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    sum = 0
    for i in range(N):
        if i < K:
            sum += max(A[i] - X, 0)
        else:
            sum += A[i]
    print(sum)

if __name__ == '__main__':
    main()