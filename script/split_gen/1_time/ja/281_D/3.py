def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = A[::-1]
    if K == 1:
        print(A[0] % D)
        return
    if N == K:
        print(A[-1] % D)
        return
    B = []
    for i in range(N-1):
        B.append(A[i] - A[i+1])
    B.sort()
    B = B[::-1]
    print((A[0] - sum(B[:K-1])) % D)
