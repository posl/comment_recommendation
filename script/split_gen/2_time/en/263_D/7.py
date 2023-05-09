def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse = True)
    B = []
    for i in range(N):
        if A[i] >= 0:
            B.append(A[i])
        else:
            break
    B.sort()
    C = []
    for i in range(N):
        if A[i] < 0:
            C.append(A[i])
        else:
            break
    C.sort(reverse = True)
    D = B + C
    for i in range(len(D)):
        if D[i] >= 0:
            D[i] = min(D[i], R)
        else:
            D[i] = max(D[i], L)
    print(sum(D))
