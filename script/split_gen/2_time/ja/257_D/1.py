def main():
    N = int(input())
    x = []
    y = []
    P = []
    for i in range(N):
        x_i, y_i, P_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        P.append(P_i)
    ans = -1
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            S = (abs(x[i] - x[j]) + abs(y[i] - y[j])) / P[i]
            if S.is_integer():
                S = int(S)
            else:
                S = int(S) + 1
            if ans < S:
                ans = S
    print(ans)
