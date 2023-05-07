def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * M
    C = [0] * M
    for i in range(M):
        B[i], C[i] = map(int, input().split())
    A.sort()
    C.sort(reverse=True)
    j = 0
    for i in range(N):
        if j < M and A[i] < C[j]:
            A[i] = C[j]
            B[j] -= 1
            if B[j] == 0:
                j += 1
        else:
            break
    print(sum(A))
