def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0 for _ in range(N)]
    for i in range(N):
        B[i] = A[i] - A[i-1]
    B = B[1:] + B[:1]
    C = [0 for _ in range(N)]
    for i in range(N):
        C[i] = (B[i] + B[i-1])//2
    print(*C)
