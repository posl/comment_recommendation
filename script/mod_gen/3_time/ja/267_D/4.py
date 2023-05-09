def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = sum(A[:i+1])
    C = [0] * (N-M+1)
    for i in range(N-M+1):
        C[i] = sum(B[i:i+M])
    print(max(C))

if __name__ == '__main__':
    main()