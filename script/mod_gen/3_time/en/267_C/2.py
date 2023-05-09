def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N - M + 1)
    for i in range(N - M + 1):
        B[i] = sum(A[i:i + M])
    print(sum(range(1, M + 1)) * max(B))

if __name__ == '__main__':
    main()