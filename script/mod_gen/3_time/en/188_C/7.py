def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [(i, a) for i, a in enumerate(A, 1)]
    for _ in range(N):
        A = [(A[i * 2 - 1][0], A[i * 2 - 1][1]) if A[i * 2 - 1][1] > A[i * 2][1] else (A[i * 2][0], A[i * 2][1]) for i in range(1, len(A) // 2 + 1)]
    print(A[0][0])

if __name__ == '__main__':
    main()