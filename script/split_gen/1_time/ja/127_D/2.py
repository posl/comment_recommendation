def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    C = []
    for _ in range(M):
        b, c = map(int, input().split())
        B.append(b)
        C.append(c)
    A.sort()
    for i in range(M):
        for j in range(B[i]):
            if A[j] < C[i]:
                A[j] = C[i]
            else:
                break
    print(sum(A))
