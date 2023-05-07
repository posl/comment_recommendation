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
    B.sort()
    C.sort(reverse=True)
    A = A + [0]*M
    B = B + [0]*N
    C = C + [0]*N
    i = 0
    j = 0
    k = 0
    while i < N and j < M:
        if A[i] < C[j]:
            A[i] = C[j]
            i += 1
            B[k] -= 1
            if B[k] == 0:
                j += 1
                k += 1
        else:
            i += 1
    print(sum(A))
