def main():
    N = int(input())
    T = [0] * (N + 1)
    K = [0] * (N + 1)
    A = [0] * (N + 1)
    for i in range(1, N + 1):
        T[i], K[i] = map(int, input().split())
        A[i] = list(map(int, input().split()))
    result = 0
    for i in range(1, N + 1):
        result = max(result, T[i] * (K[i] + 1))
    print(result)
