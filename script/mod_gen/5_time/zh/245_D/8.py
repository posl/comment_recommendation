def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0 for i in range(M+1)]
    for i in range(M+1):
        for j in range(N+1):
            B[i] += C[i+j] * A[j]
    for i in range(M+1):
        print(B[i], end=" ")
    print()

if __name__ == '__main__':
    main()