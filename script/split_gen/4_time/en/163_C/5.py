def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    for i in range(N - 1):
        B[A[i]] += 1
    for i in range(1, N + 1):
        print(B[i])
