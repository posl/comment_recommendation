def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    #print(X)
    #print(Y)
    ans = -1
    ans_m = -1
    ans_d = []
    ans_w = []
    for m in range(1, 41):
        for d in range(1, 10**13):
            w = []
            for i in range(N):
                w.append('')
            x = [0] * (m+1)
            y = [0] * (m+1)
            x[0] = 0
            y[0] = 0
            for i in range(1, m+1):
                if x[i-1] == X[0]:
                    if y[i-1] < Y[0]:
                        w[0] += 'U'
                    else:
                        w[0] += 'D'
                elif y[i-1] == Y[0]:
                    if x[i-1] < X[0]:
                        w[0] += 'R'
                    else:
                        w[0] += 'L'
                elif x[i-1] < X[0]:
                    w[0] += 'R'
                else:
                    w[0] += 'L'
                x[i], y[i] = move(x[i-1], y[i-1], w[0][-1], d)
            for i in range(1, N):
                x[0] = 0
                y[0] = 0
                for j in range(1, m+1):
                    if x[j-1] == X[i]:
                        if y[j-1] < Y[i]:
                            w[i] += 'U'
                        else:
                            w[i] += 'D'
                    elif y[j-1] == Y[i]:
                        if x[j-1] < X[i]:
                            w[i] += 'R'
                        else:
                            w[i] += 'L'
                    elif x[j-1] < X[i]:
                        w[i] += 'R'
                    else:
                        w[i] += 'L'
                    x[j], y[j] = move(x[j-1], y[j-1], w[i][-1],
