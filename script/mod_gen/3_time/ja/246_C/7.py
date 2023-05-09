def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = 0
    for i in range(N):
        if i < K:
            total += max(A[i] - X, 0)
        else:
            total += A[i]
    print(total)

if __name__ == '__main__':
    main()