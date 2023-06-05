def main():
    N, K = input().split()
    N = int(N)
    K = int(K)
    if K == 1:
        print(N+1)
        return
    if K == N+1:
        print(1)
        return
    if K == 2:
        print((N+1)*(N+2)//2)
        return
    if K >= N//2:
        K = N - K + 2
    print(K*(N-K+2))
