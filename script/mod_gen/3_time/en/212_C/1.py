def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    min_diff = abs(A[0] - B[0])
    while i < N and j < M:
        diff = abs(A[i] - B[j])
        if diff < min_diff:
            min_diff = diff
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    print(min_diff)

if __name__ == '__main__':
    main()