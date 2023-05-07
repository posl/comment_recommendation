def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [C[i] for i in range(N, N+M+1)]
    for i in range(M):
        B[i] -= sum([A[j]*B[i+j+1] for j in range(N)])
        B[i] //= A[0]
    print(' '.join(map(str, B)))

if __name__ == '__main__':
    main()