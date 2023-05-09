def main():
    X, K = map(int, input().split())
    for i in range(K):
        X = (X // 10) * 10 if X % 10 < 5 else (X // 10 + 1) * 10
    print(X)
