def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "U":
            X //= 2
        elif S[i] == "L":
            X = (X-1)//2
        elif S[i] == "R":
            X = (X-1)//2 + 1
    print(X)
