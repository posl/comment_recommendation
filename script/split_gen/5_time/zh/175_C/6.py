def main():
    X, K, D = map(int, input().split())
    if X > 0:
        if X - K * D > 0:
            print(X - K * D)
        else:
            print(abs(X - K * D))
    elif X < 0:
        if X + K * D < 0:
            print(abs(X + K * D))
        else:
            print(X + K * D)
    else:
        print(abs(X + K * D))
