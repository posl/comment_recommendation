def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    A.sort(reverse=True)
    if A[M-1] >= total / (4*M):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()