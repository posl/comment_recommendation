def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for i in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort()
    C.sort(reverse=True)
    # print(A)
    # print(B)
    # print(C)
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] < C[j]:
            A[i] = C[j]
            B[j] -= 1
            if B[j] == 0:
                j += 1
        i += 1
    print(sum(A))
