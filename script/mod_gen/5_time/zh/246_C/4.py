def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    result = 0
    for i in range(K):
        if A[i] >= X:
            result += A[i] - X
        else:
            result += 0
    print(result)

if __name__ == '__main__':
    main()