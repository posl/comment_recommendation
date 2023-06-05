def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    total = 0
    for i in range(N):
        if K > 0:
            total += max(A[i] - X, 0)
            K -= 1
        else:
            total += A[i]
    print(total)

if __name__ == '__main__':
    main()