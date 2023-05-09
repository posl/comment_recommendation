def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if M == 0:
        print(1)
        return
    A.sort()
    A = [0] + A + [N + 1]
    D = [A[i + 1] - A[i] - 1 for i in range(M + 1)]
    D = [d for d in D if d != 0]
    K = max(D)
    print((sum(D) + K - 1) // K + 1)
