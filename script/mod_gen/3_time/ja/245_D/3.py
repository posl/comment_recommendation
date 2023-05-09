def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0 for _ in range(M+1)]
    for i in range(N+M, -1, -1):
        B[M-(N+M-i)] = int((C[i] - sum([A[j]*(i-j) for j in range(N+1)])) / A[N])
    print(*B)

if __name__ == '__main__':
    main()