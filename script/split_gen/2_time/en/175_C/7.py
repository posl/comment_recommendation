def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X < K*D:
        if (K - X//D) % 2 == 1:
            print(X%D - D)
        else:
            print(X%D)
    else:
        print(X - K*D)
