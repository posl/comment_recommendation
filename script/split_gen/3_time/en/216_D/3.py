def solve():
    N, M = map(int, input().split())
    K = [0] * M
    A = [0] * M
    for i in range(M):
        K[i] = int(input())
        A[i] = list(map(int, input().split()))
    #print(N, M, K, A)
    #print
