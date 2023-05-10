def main():
    # input
    X, K, D = map(int, input().split())
    # compute
    X = abs(X)
    if X // D > K:
        ans = X - D * K
    else:
        if (K - X // D) % 2 == 0:
            ans = X % D
        else:
            ans = D - X % D
    # output
    print(ans)
