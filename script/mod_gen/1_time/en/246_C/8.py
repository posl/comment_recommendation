def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    for i in range(N):
        if A[i] >= X:
            A[i] -= X
            K -= 1
        else:
            break
    if K > 0:
        for i in range(N):
            if A[i] > 0:
                if K >= A[i] // X:
                    K -= A[i] // X
                    A[i] %= X
                else:
                    A[i] -= K * X
                    K = 0
    print(sum(A))

if __name__ == '__main__':
    main()