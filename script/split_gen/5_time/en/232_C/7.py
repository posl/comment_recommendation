def main():
    N,M = map(int,input().split())
    A = [list(map(int,input().split())) for i in range(M)]
    C = [list(map(int,input().split())) for i in range(M)]
    for i in range(2**N):
        P = []
        for j in range(N):
            if (i >> j) & 1:
                P.append(j+1)
        if len(P) == N:
            flg = True
            for a,b in A:
                if not (a in P and b in P):
                    flg = False
            for c,d in C:
                if not (c in P and d in P):
                    flg = False
            if flg:
                print("Yes")
                return
    print("No")
