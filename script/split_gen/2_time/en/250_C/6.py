def main():
    N, Q = map(int, input().split())
    A = [0] * (N + 1)
    B = [0] * (N + 1)
    for i in range(1, N+1):
        A[i] = i
        B[i] = i
    for _ in range(Q):
        x = int(input())
        A[x], A[x+1] = A[x+1], A[x]
    for i in range(1, N+1):
        print(A[i], end=' ')
    print()
