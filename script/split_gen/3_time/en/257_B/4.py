def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    result = [0] * N
    for i in range(K):
        result[A[i]-1] += 1
    for i in range(N):
        if result[i] > 0:
            result[i] = result[i] - Q + K
    for i in range(N):
        if result[i] > 0:
            print("Yes")
        else:
            print("No")
