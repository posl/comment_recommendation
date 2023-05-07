def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "U":
            if X % 2 == 1:
                X = (X - 1) // 2
        elif S[i] == "L":
            X = X * 2 + 1
        elif S[i] == "R":
            X = X * 2
    print(X)
