def main():
    N, M = map(int, input().split())
    X = list(map(int, input().split()))
    X.sort()
    x = X[0]
    for i in range(1, M):
        x = X[i] - x
    print(x)
