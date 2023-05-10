def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == "U":
            X = X // 2
        elif s == "L":
            X = X * 2
        else:
            X = X * 2 + 1
    print(X)
