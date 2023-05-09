def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [A[i]+B[i] for i in range(N)]
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    a = []
    b = []
    c = []
    for i in range(N):
        if A[i] in a:
            continue
        else:
            a.append(A[i])
            if len(a) == X:
                break
    for i in range(N):
        if B[i] in b:
            continue
        else:
            b.append(B[i])
            if len(b) == Y:
                break
    for i in range(N):
        if C[i] in c:
            continue
        else:
            c.append(C[i])
            if len(c) == Z:
                break
    for i in range(N):
        if A[i] in a and B[i] in b and C[i] in c:
            print(i+1)
