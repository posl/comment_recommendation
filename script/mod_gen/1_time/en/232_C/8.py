def isSameShape(N, M, A, B, C, D):
    P = [0] * N
    for i in range(N):
        P[i] = i + 1
    for i in range(N):
        for j in range(N):
            if A[i] == C[j]:
                if B[i] == D[j]:
                    continue
                else:
                    return False
            elif A[i] == D[j]:
                if B[i] == C[j]:
                    continue
                else:
                    return False
            elif B[i] == C[j]:
                if A[i] == D[j]:
                    continue
                else:
                    return False
            elif B[i] == D[j]:
                if A[i] == C[j]:
                    continue
                else:
                    return False
            else:
                return False
    return True

if __name__ == '__main__':
    isSameShape()