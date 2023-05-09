def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for _ in range(N)]
    B[0] = sum(A) // (N-1)
    for i in range(N-1):
        B[i+1] = A[i] - B[i]
    print(*B)
