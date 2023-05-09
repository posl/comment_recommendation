def main():
    N, M = map(int, input().split())
    A = [0] * N
    for _ in range(M):
        B = list(map(int, input().split()))
        for b in B[1:]:
            A[b-1] += 1
    print('Yes' if max(A) > 1 else 'No')

if __name__ == '__main__':
    main()