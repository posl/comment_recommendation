def main():
    X, A, D, N = map(int, input().split())
    S = [A + D * i for i in range(N)]
    if X in S:
        print(0)
    else:
        if X < min(S):
            print(min(S) - X)
        elif X > max(S):
            print(X - max(S))
        else:
            print(min(X - min(S), max(S) - X))
