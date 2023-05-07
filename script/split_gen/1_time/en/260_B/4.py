def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [i for i in range(1, N+1)]
    D = list(zip(A, B, C))
    D.sort(key=lambda x: x[0], reverse=True)
    D.sort(key=lambda x: x[1], reverse=True)
    D.sort(key=lambda x: x[0]+x[1], reverse=True)
    for i in range(X+Y+Z):
        print(D[i][2])
