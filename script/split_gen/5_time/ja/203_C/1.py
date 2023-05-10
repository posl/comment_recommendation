def main():
    N, K = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    i = 0
    while K >= B[i]:
        K -= B[i]
        i += 1
        if i == N:
            break
    print(A[i - 1] + K + 1)
