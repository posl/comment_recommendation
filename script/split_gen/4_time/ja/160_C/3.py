def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    max_distance = 0
    for i in range(N):
        if i == N - 1:
            distance = K - A[i] + A[0]
        else:
            distance = A[i + 1] - A[i]
        if distance > max_distance:
            max_distance = distance
    print(K - max_distance)
