def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    total = sum(A)
    print('Yes' if A[M-1] >= total/(4*M) else 'No')

if __name__ == '__main__':
    main()