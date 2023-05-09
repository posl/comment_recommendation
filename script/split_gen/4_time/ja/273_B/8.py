def main():
    X, K = map(int, input().split())
    for i in range(K):
        if X % 10 ** i != 0:
            X = X // 10 ** i * 10 ** i
        else:
            continue
    print(X)
