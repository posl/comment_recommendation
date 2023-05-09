def main():
    A, B, X = map(int, input().split())
    #print(A, B, X)
    #print("A*X", A*X)
    #print("B*d(N)", B*d(N))
    #print("A*X+B*d(N)", A*X+B*d(N))
    #print("A*X+B*d(N) <= X", A*X+B*d(N) <= X)
    #print("A*X+B*d(N) <= X", A*X+B*d(N) <= X)
    if A*X < X:
        #print("A*X < X")
        print(0)
        return
    #print("A*X >= X")
    #print("X/(A+B)", X/(A+B))
    #print("int(X/(A+B))", int(X/(A+B)))
    N = int(X/(A+B))
    #print("N", N)
    while A*N+B*d(N) <= X:
        N += 1
    N -= 1
    print(N)
