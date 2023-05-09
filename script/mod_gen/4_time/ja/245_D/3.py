def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0 for i in range(M+1)]
    B[0] = C[0] // A[0]
    for i in range(1, M+1):
        B[i] = (C[i] - sum([B[j] * A[i-j] for j in range(i)])) // A[0]
    print(*B)

if __name__ == '__main__':
    main()