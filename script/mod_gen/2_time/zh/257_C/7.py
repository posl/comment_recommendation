def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    result = [0] * K
    for i in range(K):
        result[i] = A[L[i] - 1]
    for i in range(Q):
        if result.count(result[i]) > 1:
            continue
        else:
            for j in range(i + 1, Q):
                if result[i] == result[j]:
                    result[j] = result[i]
    result.sort()
    print(*result)

if __name__ == '__main__':
    main()