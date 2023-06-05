def main():
    N,X,Y = map(int,input().split())
    U = [0] * (N-1)
    V = [0] * (N-1)
    for i in range(N-1):
        U[i],V[i] = map(int,input().split())
    print(U)
    print(V)
    print(N,X,Y)
