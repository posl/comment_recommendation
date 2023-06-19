def main():
    n = int(input())
    x, y, h = [0] * n, [0] * n, [0] * n
    for i in range(n):
        x[i], y[i], h[i] = map(int, input().split())
    for C_X in range(101):
        for C_Y in range(101):
            H = 0
            while h[0] == 0:
                H += 1
                for i in range(n):
                    if h[i] != max(H - abs(x[i] - C_X) - abs(y[i] - C_Y), 0):
                        break
                else:
                    print(C_X, C_Y, H)
                    return

if __name__ == '__main__':
    main()