def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0]*(M+1)
    for i in range(M+1):
        B[i] = C[i]
        for j in range(i):
            B[i] -= A[j]*B[i-j-1]
        B[i] //= A[i]
    print(*B)

if __name__ == '__main__':
    main()