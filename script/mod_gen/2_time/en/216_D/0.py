def main():
    N, M = map(int, input().split())
    K = [0] * M
    A = [0] * M
    for i in range(M):
        K[i] = int(input())
        A[i] = list(map(int, input().split()))
    #print(N, M, K, A)
    #print(A)
    #print(sum(K))
    #print(sum(K) == 2*N)
    #print(len(A))
    #print(len(A) == M)
    #print(all([len(A[i]) == K[i] for i in range(M)]))
    if not (sum(K) == 2*N and len(A) == M and all([len(A[i]) == K[i] for i in range(M)])):
        print("No")
        return
    #print("Yes")
    #print(A)
    #print([A[i][0] for i in range(M)])
    #print([A[i][0] for i in range(M)].count(1))
    #print([A[i][0] for i in range(M)].count(2))
    #print([A[i][0] for i in range(M)].count(3))
    #print([A[i][0] for i in range(M)].count(4))
    #print([A[i][0] for i in range(M)].count(5))
    #print([A[i][0] for i in range(M)].count(6))
    #print([A[i][0] for i in range(M)].count(7))
    #print([A[i][0] for i in range(M)].count(8))
    #print([A[i][0] for i in range(M)].count(9))
    #print([A[i][0] for i in range(M)].count(10))
    #print([A[i][0] for i in range(M)].count(11))
    #print([A[i][0] for i in range(M)].count(12))
    #print([A[i][0] for i in range(M)].count(13))
    #print([A[i][0] for i in range(M)].count(14))
    #print([A[i][0] for i in range(M)].count(15))
    #print([A[i][0] for i in range(M)].count(16

if __name__ == '__main__':
    main()