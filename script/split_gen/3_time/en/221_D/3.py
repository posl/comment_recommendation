def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    C = [0] * (10**5 + 1)
    for i in range(N):
        C[A[i]] += 1
        C[A[i] + B[i]] -= 1
    for i in range(1, 10**5 + 1):
        C[i] += C[i - 1]
    D = [0] * (N + 1)
    for i in range(1, 10**5 + 1):
        D[C[i]] += 1
    for i in range(1, N + 1):
        D[i] += D[i - 1]
    print(*D[1:])
