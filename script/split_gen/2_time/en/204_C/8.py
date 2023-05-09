def main():
    import sys
    import numpy as np
    from scipy.sparse.csgraph import floyd_warshall
    input = sys.stdin.readline
    N,M = map(int,input().split())
    A,B = [],[]
    for _ in range(M):
        a,b = map(int,input().split())
        A.append(a-1)
        B.append(b-1)
    A = np.array(A)
    B = np.array(B)
    G = np.zeros((N,N),dtype=np.int64)
    G[A,B] = 1
    G[B,A] = 1
    G = floyd_warshall(G)
    G = np.where(G < float("inf"),1,0)
    print(int(np.sum(G*(N-G-1))))
