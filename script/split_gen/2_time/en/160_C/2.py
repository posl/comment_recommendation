def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    distance = []
    for i in range(N - 1):
        distance.append(A[i + 1] - A[i])
    distance.append(A[0] + K - A[N - 1])
    print(K - max(distance))
