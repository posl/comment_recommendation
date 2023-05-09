def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = sum(A)
    for i in range(N - 1):
        if A[i] >= M:
            break
        A[i + 1] = min(A[i + 1], A[i] * 2)
    print(ans - sum(A))

if __name__ == '__main__':
    main()