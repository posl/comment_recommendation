def main():
    Q = int(input())
    P = []
    X = []
    for _ in range(Q):
        p, *x = map(int, input().split())
        P.append(p)
        X.append(x[0] if x else None)
    #print(P)
    #print(X)
    A = []
    for i in range(Q):
        if P[i] == 1:
            A.append(X[i])
        elif P[i] == 2:
            A = [x + X[i] for x in A]
        else:
            A.sort()
            print(A.pop(0))
    return
main()
