def main():
    N,X,Y,Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted([A[i],i+1] for i in range(N))
    B = sorted([B[i],i+1] for i in range(N))
    AB = sorted([[A[i][0]+B[i][0],A[i][1]] for i in range(N)])
    a = []
    for i in range(X):
        a.append(A.pop()[1])
    for i in range(Y):
        a.append(B.pop()[1])
    for i in range(Z):
        a.append(AB.pop()[1])
    a.sort()
    for i in a:
        print(i)
