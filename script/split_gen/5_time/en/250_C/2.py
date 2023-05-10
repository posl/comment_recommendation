def main():
    N, Q = map(int, input().split())
    A = [int(input()) for _ in range(Q)]
    for i in range(Q-1, -1, -1):
        A[i], A[i-1] = A[i-1], A[i]
    for i in range(1, N+1):
        if i in A:
            print(i, end=' ')
    for i in range(1, N+1):
        if i not in A:
            print(i, end=' ')
    print()
