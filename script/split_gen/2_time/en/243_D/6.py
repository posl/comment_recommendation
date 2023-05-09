def main():
    N, X = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == "U":
            X = X // 2
        elif S[i] == "L":
            X = X * 2 - 1
        else:
            X = X * 2
    print(X)
