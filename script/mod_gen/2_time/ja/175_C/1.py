def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X // D >= K:
        print(X - D * K)
    else:
        if (K - X // D) % 2 == 0:
            print(X - X // D * D)
        else:
            print(X - (X // D + 1) * D)
main()
