def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if M == N:
        print(0)
        return
    if M == 1:
        print(min(A[0], N - A[0] + 1))
        return
    B = [0] * (M - 1)
    for i in range(M - 1):
        B[i] = A[i + 1] - A[i] - 1
    B.sort()
    print(B[0] + 1)
