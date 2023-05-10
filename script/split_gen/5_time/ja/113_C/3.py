def main():
    N, M = map(int, input().split())
    P = []
    Y = []
    for _ in range(M):
        p, y = map(int, input().split())
        P.append(p)
        Y.append(y)
    #print(P)
    #print(Y)
    P_Y = [(P[i], Y[i]) for i in range(M)]
    #print(P_Y)
    P_Y.sort()
    #print(P_Y)
    d = {}
    for i in range(M):
        p, y = P_Y[i]
        if p not in d.keys():
            d[p] = 1
        else:
            d[p] += 1
        p_y = str(p).zfill(6) + str(d[p]).zfill(6)
        print(p_y)
