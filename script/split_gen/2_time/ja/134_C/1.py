def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    for i in range(N):
        if A[i] == maxA:
            A[i] = 0
    maxA = max(A)
    for i in range(N):
        print(maxA)
