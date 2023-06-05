def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    C = list(map(int,input().split()))
    P.insert(0,0)
    C.insert(0,0)
    ans = -float("inf")
    for i in range(1,N+1):
        loop = []
        loop.append(C[i])
        loop.append(C[P[i]])
        loop.append(C[P[P[i]]])
        if K>=3:
            loop.append(C[P[P[P[i]]]])
        if K>=4:
            loop.append(C[P[P[P[P[i]]]]])
        if K>=5:
            loop.append(C[P[P[P[P[P[i]]]]]])
        if K>=6:
            loop.append(C[P[P[P[P[P[P[i]]]]]]])
        if K>=7:
            loop.append(C[P[P[P[P[P[P[P[i]]]]]]]])
        if K>=8:
            loop.append(C[P[P[P[P[P[P[P[P[i]]]]]]]]])
        if K>=9:
            loop.append(C[P[P[P[P[P[P[P[P[P[i]]]]]]]]]])
        if K>=10:
