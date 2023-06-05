def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    C = list(map(int,input().split()))
    B = [0] * (M+1)
    for i in range(N+1):
        B[0] += A[i] * C[i]
    for i in range(1,M+1):
        B[i] = C[N+i] - B[0]
    print(*B)

if __name__ == '__main__':
    main()