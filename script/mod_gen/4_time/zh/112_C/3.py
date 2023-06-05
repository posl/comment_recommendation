def main():
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    for i in range(N):
        if data[i][2] != 0:
            x, y, h = data[i]
            break
    for C_X in range(101):
        for C_Y in range(101):
            H = h + abs(C_X - x) + abs(C_Y - y)
            for i in range(N):
                if data[i][2] != max(H - abs(C_X - data[i][0]) - abs(C_Y - data[i][1]), 0):
                    break
            else:
                print(C_X, C_Y, H)
                exit()

if __name__ == '__main__':
    main()