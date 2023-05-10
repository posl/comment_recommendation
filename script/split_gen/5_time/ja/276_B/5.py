def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(1, N+1):
        l = []
        for j in range(M):
            if i == A[j]:
                l.append(B[j])
            elif i == B[j]:
                l.append(A[j])
        l.sort()
        print(len(l), *l)
