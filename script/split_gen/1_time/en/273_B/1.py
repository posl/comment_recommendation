def main():
    X, K = map(int, input().split())
    for i in range(K):
        if X % 10 == 0:
            X = X // 10
        else:
            X -= 1
    print(X)
