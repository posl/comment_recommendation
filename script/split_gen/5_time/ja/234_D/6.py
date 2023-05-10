def main():
    N,K=map(int,input().split())
    P=list(map(int,input().split()))
    p=P[:K]
    p.sort()
    for i in range(K,N):
        p.append(P[i])
        p.sort()
        p.pop(0)
        print(p[0])
