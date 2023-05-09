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
                if h[i] != 0:
                    H = h[i] + abs(C_X - x[i]) + abs(C_Y - y[i])
                    break
            for i in range(N):
                if h[i] != max(H - abs(C_X - x[i]) - abs(C_Y - y[i]), 0):
                    break
            else:
                print(C_X, C_Y, H)
                return
