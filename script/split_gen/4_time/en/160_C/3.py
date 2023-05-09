def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    max_d = 0
    for i in range(N):
        d = A[i+1] - A[i]
        if max_d < d:
            max_d = d
    print(K - max_d)
