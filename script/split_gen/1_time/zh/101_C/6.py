def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    min = 1000000000
    for i in range(N-K+1):
        if min > A[i+K-1] - A[i]:
            min = A[i+K-1] - A[i]
    print(min)
