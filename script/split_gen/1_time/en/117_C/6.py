def main():
    N, M = map(int, input().split())
    X = sorted(map(int, input().split()))
    if N >= M:
        print(0)
        return
    D = [0] * (M-1)
    for i in range(M-1):
        D[i] = X[i+1] - X[i]
    D.sort()
    print(sum(D[:M-N]))
