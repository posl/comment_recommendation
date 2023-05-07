def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    C = [0] * N
    for i in range(N):
        C[i] = A[i] - (i + 1)
    #print(C)
    for i in range(N):
        if C[i] >= K:
            print(K + i)
            K = 0
            break
        else:
            K -= C[i]
    if K > 0:
        for i in range(N):
            print(A[i] + K // N + int(i < K % N))

if __name__ == '__main__':
    main()