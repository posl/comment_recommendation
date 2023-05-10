def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = 0
    for i in range(K):
        result = result + A[i] * (N // A[i])
        N = N % A[i]
    print(result)
