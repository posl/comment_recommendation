def main():
    N,X,Y = map(int, input().split())
    X -= 1
    Y -= 1
    U = [0] * (N-1)
    V = [0] * (N-1)
    for i in range(N-1):
        U[i],V[i] = map(int, input().split())
        U[i] -= 1
        V[i] -= 1
    XtoY = [0] * N
    XtoY[X] = 1
    for i in range(N-1):
        if U[i] == X:
            XtoY[V[i]] = XtoY[U[i]] + 1
        elif V[i] == X:
            XtoY[U[i]] = XtoY[V[i]] + 1
        else:
            pass
    XtoY[Y] = 1
    for i in range(N-1):
        if U[i] == Y:
            XtoY[V[i]] = XtoY[U[i]] + 1
        elif V[i] == Y:
            XtoY[U[i]] = XtoY[V[i]] + 1
        else:
            pass
    for i in range(N):
        if XtoY[i] == 0:
            XtoY[i] = 1
        else:
            pass
    XtoY[X] = 0
    XtoY[Y] = 0
    for i in range(N):
        if XtoY[i] == 1:
            print(i+1,end=" ")
        else:
            pass
