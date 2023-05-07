def main():
    N = int(input())
    V = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    X = []
    for i in range(N):
        if V[i] > C[i]:
            X.append(V[i] - C[i])
    print(sum(X))
