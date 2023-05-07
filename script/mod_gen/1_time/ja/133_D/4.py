def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for i in range(N)]
    for i in range(N):
        B[i] = A[i] - A[(i+1)%N]
    C = [0 for i in range(N)]
    for i in range(N):
        C[i] = (B[i] + B[(i-1)%N])//2
    print(*C)

if __name__ == '__main__':
    main()