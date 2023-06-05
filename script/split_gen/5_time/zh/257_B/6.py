def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    for i in range(1, Q + 1):
        if A[L[i - 1] - 1] < N and (A[L[i - 1] - 1] + 1) not in A:
            A[L[i - 1] - 1] += 1
    for i in range(K):
        print(A[i], end=" ")
    print()
