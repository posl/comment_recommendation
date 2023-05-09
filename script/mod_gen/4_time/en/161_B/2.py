def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = 0
    for a in A:
        total += a
    for i in range(M):
        if A[i] < total / (4 * M):
            print('No')
            return
    print('Yes')

if __name__ == '__main__':
    main()