def main():
    X, K = map(int, input().split())
    for i in range(K):
        X = round(X, -i)
    print(X)
