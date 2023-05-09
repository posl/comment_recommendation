def main():
    N = int(input())
    A = []
    P = []
    X = []
    for i in range(N):
        a,p,x = map(int,input().split())
        A.append(a)
        P.append(p)
        X.append(x)
    cost = -1
    for i in range(N):
        if X[i] > 0:
            if cost == -1:
                cost = P[i]
            else:
                cost = min(cost,P[i])
    print(cost)
