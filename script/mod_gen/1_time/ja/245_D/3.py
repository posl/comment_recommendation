def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0 for _ in range(M+1)]
    for i in range(M+1):
        B[i] = C[i+N] - sum([A[j] * B[i-j] for j in range(i)])
        B[i] //= A[0]
    print(*B)

if __name__ == '__main__':
    main()