def main():
    N, X = map(int, input().split())
    S = input()
    i = 0
    while i < N:
        if S[i] == "U":
            i += 1
        elif S[i] == "L":
            X = X * 2
            i += 1
        else:
            X = X * 2 + 2
            i += 1
    print(X)
