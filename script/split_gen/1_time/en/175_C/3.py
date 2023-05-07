def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X // D > K:
        print(X - K * D)
    else:
        if (K - X // D) % 2 == 0:
            print(X % D)
        else:
            print(abs(X % D - D))
