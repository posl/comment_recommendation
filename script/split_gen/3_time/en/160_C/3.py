def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    d = []
    for i in range(N):
        d.append(A[i+1] - A[i])
    print(K - max(d))
