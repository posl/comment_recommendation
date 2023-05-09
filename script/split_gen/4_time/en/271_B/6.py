def main():
    N,Q = map(int,input().split())
    L = []
    A = []
    for i in range(N):
        L.append(list(map(int,input().split())))
        A.append(list(map(int,input().split())))
    for i in range(Q):
        print(L[A[i][0]-1][A[i][1]-1])
