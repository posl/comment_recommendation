def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    max = 0
    for i in range(N):
        if A[i+1] - A[i] > max:
            max = A[i+1] - A[i]
    print(K - max)