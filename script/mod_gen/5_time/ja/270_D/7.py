def game(N,K,A):
    count = 0
    while N > 0:
        for i in range(K):
            if N >= A[K-i-1]:
                N -= A[K-i-1]
                count += A[K-i-1]
                break
    return count
N,K = map(int,input().split())
A = list(map(int,input().split()))
print(game(N,K,A))
