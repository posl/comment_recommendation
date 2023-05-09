def main():
    N,M = map(int,input().split())
    L = [0]*M
    R = [0]*M
    for i in range(M):
        L[i],R[i] = map(int,input().split())
    Lmax = max(L)
    Rmin = min(R)
    if Rmin-Lmax+1>0:
        print(Rmin-Lmax+1)
    else:
        print(0)
