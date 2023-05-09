def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    C = [0] * M
    for i in range(M):
        B[i], C[i] = map(int, input().split())
    A.sort()
    C.sort(reverse=True)
    for i in range(M):
        for j in range(B[i]):
            if A[j] < C[i]:
                A[j] = C[i]
            else:
                break
    print(sum(A))
