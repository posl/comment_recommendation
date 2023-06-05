def main():
    N,X,Y = map(int,input().split())
    U = []
    V = []
    for i in range(N-1):
        u,v = map(int,input().split())
        U.append(u)
        V.append(v)
    print(U)
    print(V)
