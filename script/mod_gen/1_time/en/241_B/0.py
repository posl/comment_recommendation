def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] >= B[j]:
            j += 1
        i += 1
    if j == M:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()