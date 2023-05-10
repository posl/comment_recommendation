def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = [(A[i], B[i], i+1) for i in range(N)]
    AB.sort(key = lambda x: x[2])
    AB.sort(key = lambda x: x[1], reverse=True)
    AB.sort(key = lambda x: x[0], reverse=True)
    for i in range(X):
        print(AB[i][2])
    for i in range(Y):
        print(AB[i+X][2])
    for i in range(Z):
        print(AB[i+X+Y][2])
