def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == "U":
            if X % 2 == 0:
                X = X // 2
        elif s == "L":
            X = X * 2
        elif s == "R":
            X = X * 2 + 1
    print(X)
