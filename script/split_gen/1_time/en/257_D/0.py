def main():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    P = [0]*N
    for i in range(N):
        X[i], Y[i], P[i] = map(int, input().split())
    print(solve(N, X, Y, P))
