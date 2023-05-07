def main():
    N,X,Y,Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    AB = []
    for i in range(N):
        AB.append([A[i], B[i], i+1])
    AB.sort(reverse=True)
    AB = AB[:X+Y+Z]
    AB.sort(key=lambda x: x[2])
    for i in range(X):
        print(AB[i][2])
    for i in range(X, X+Y):
        print(AB[i][2])
    for i in range(X+Y, X+Y+Z):
        print(AB[i][2])
