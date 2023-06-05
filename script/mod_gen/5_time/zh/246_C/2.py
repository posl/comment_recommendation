def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    count = 0
    for i in range(N):
        if K > 0:
            count += max(A[i] - X, 0)
            K -= 1
        else:
            count += A[i]
    print(count)

if __name__ == '__main__':
    main()