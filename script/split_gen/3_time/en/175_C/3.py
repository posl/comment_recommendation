def main():
    X, K, D = map(int, input().split())
    X = abs(X)
    if X // D >= K:
        print(X - D * K)
        return
    K -= X // D
    X %= D
    if K % 2 == 0:
        print(X)
    else:
        print(abs(X - D))
