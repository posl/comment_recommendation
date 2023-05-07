def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    S = input()
    for i in range(N):
        if S[i] == "L":
            for j in range(i+1, N):
                if S[j] == "R":
                    if X[i] < X[j]:
                        if Y[i] == Y[j]:
                            print("Yes")
                            exit()
    print("No")
