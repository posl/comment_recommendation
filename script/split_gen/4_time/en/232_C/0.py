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
    ans = "No"
    for i in range(2**N):
        P = []
        for j in range(N):
            if ((i >> j) & 1):
                P.append(1)
            else:
                P.append(0)
        for j in range(N):
            if P[j] == 0:
                continue
            for k in range(N):
                if P[k] == 0:
                    continue
                if j == k:
                    continue
                if (j+1 in A and k+1 in B) or (j+1 in B and k+1 in A):
                    continue
                else:
                    P[j] = 0
                    P[k] = 0
                    break
        for j in range(N):
            if P[j] == 0:
                continue
            for k in range(N):
                if P[k] == 0:
                    continue
                if j == k:
                    continue
                if (j+1 in C and k+1 in D) or (j+1 in D and k+1 in C):
                    continue
                else:
                    P[j] = 0
                    P[k] = 0
                    break
        if 1 not in P:
            ans = "Yes"
            break
    print(ans)
