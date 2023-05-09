def main():
    N = int(input())
    if N < 3:
        print("No")
        return
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if (Y[j] - Y[i]) * (X[k] - X[j]) == (X[j] - X[i]) * (Y[k] - Y[j]):
                    print("Yes")
                    return
    print("No")
    return
