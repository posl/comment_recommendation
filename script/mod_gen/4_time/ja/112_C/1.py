def main():
    N = int(input())
    x = [0] * N
    y = [0] * N
    h = [0] * N
    for i in range(N):
        x[i], y[i], h[i] = map(int, input().split())
    for C_X in range(101):
        for C_Y in range(101):
            H = h[0] + abs(x[0] - C_X) + abs(y[0] - C_Y)
            if all(h[i] == max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0) for i in range(N)):
                print(C_X, C_Y, H)
                return

if __name__ == '__main__':
    main()