def main():
    N = int(input())
    x, y, P = [], [], []
    for i in range(N):
        x_i, y_i, P_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        P.append(P_i)
    S = 0
    for i in range(N):
        for j in range(N):
            if P[i] * S >= abs(x[i] - x[j]) + abs(y[i] - y[j]):
                if i == j:
                    break
                else:
                    S += 1
                    break
    print(S)
