def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = [0] * (2 * N + 1)
    for i in range(N):
        result[A[i]] = i + 1
    for i in range(1, N + 1):
        k = i
        while k != 1:
            k = k // 2
            result[k] = max(result[2 * k], result[2 * k + 1]) + 1
    for i in range(1, 2 * N + 1):
        print(result[i])

if __name__ == '__main__':
    main()