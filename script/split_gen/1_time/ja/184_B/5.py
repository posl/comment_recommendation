def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "o":
            X += 1
        elif X != 0:
            X -= 1
    print(X)
