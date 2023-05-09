def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    for i in range(M):
        if A[i] < total / (4 * M):
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()