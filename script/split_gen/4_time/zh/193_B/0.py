def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a, p, x = map(int, input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    minP = 1000000000
    for i in range(N):
        if X[i] > 0:
            if P[i] < minP:
                minP = P[i]
    if minP == 1000000000:
        print(-1)
    else:
        print(minP)
