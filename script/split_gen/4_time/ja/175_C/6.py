def main():
    # input
    X, K, D = map(int, input().split())
    # compute
    if X < 0:
        X = -X
    if X//D >= K:
        print(X-K*D)
    else:
        if (K-X//D)%2 == 0:
            print(X%D)
        else:
            print(D-X%D)
