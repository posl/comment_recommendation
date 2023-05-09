def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[i] = max(A[i], L)
        B[i] = min(B[i], R)
    print(sum(B))

if __name__ == '__main__':
    main()