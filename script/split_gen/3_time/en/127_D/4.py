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
    C.sort()
    C.reverse()
    B.sort()
    B.reverse()
    idx = 0
    for i in range(M):
        for j in range(B[i]):
            if idx >= N:
                break
            if A[idx] < C[i]:
                A[idx] = C[i]
                idx += 1
            else:
                break
    print(sum(A))
