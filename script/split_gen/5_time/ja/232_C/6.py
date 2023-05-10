def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    if M == 0:
        print("Yes")
        return
    for i in range(1 << N):
        P = []
        for j in range(N):
            if i & (1 << j):
                P.append(j + 1)
        if len(P) != N:
            continue
        if check(A, B, C, D, P):
            print("Yes")
            return
    print("No")
