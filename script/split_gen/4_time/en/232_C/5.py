def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for m in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for m in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    for n in range(2**N):
        flag = True
        for m in range(M):
            if not (((n >> (A[m]-1)) & 1) == ((n >> (B[m]-1)) & 1)):
                flag = False
                break
        if flag:
            for m in range(M):
                if not (((n >> (C[m]-1)) & 1) == ((n >> (D[m]-1)) & 1)):
                    flag = False
                    break
        if flag:
            print("Yes")
            return
    print("No")
