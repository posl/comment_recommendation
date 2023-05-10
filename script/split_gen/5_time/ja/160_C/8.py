def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    max_distance = 0
    for i in range(N):
        max_distance = max(max_distance, A[i+1] - A[i])
    print(K - max_distance)
