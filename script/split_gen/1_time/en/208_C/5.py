def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = [K // N] * N
    K %= N
    for i in range(K):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])
