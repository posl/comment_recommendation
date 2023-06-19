def main():
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    if N == 1:
        print(0)
        print(0)
        print("U")
        return
    for m in range(1, 41):
        for i in range(1, N):
            if abs(X[i] - X[i-1]) + abs(Y[i] - Y[i-1]) != m:
                break
        else:
            break
    else:
        print(-1)
        return
    print(m)
    d = [abs(X[i] - X[i-1]) + abs(Y[i] - Y[i-1]) for i in range(1, N)]
    print(" ".join(map(str, d)))
    for x, y in zip(X[1:], Y[1:]):
        s = ""
        if x > X[0]:
            s += "R" * (x - X[0])
        elif x < X[0]:
            s += "L" * (X[0] - x)
        if y > Y[0]:
            s += "U" * (y - Y[0])
        elif y < Y[0]:
            s += "D" * (Y[0] - y)
        print(s)
