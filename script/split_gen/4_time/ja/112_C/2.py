def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    h = [0] * N
    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            for i in range(N):
                if h[i] == 0:
                    continue
                else:
                    tmp = h[i] + abs(x[i] - C_X) + abs(y[i] - C_Y)
                    if H == 0:
                        H = tmp
                    elif H != tmp:
                        break
            else:
                print(C_X, C_Y, H)
                exit()
