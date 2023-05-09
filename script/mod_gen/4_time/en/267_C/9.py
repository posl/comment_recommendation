def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A, reverse=True)
    A = A[:M]
    A = sorted(A)
    result = 0
    for i in range(len(A)):
        result += (i + 1) * A[i]
    print(result)

if __name__ == '__main__':
    main()