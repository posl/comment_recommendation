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
    S = 0
    while True:
        S += 1
        flag = True
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if P[i] * S < abs(x[i] - x[j]) + abs(y[i] - y[j]):
                    flag = False
                    break
            if not flag:
                break
        if flag:
            break
    print(S)
