def main():
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    for C_X in range(101):
        for C_Y in range(101):
            for i in range(N):
                if data[i][2] > 0:
                    H = data[i][2] + abs(data[i][0] - C_X) + abs(data[i][1] - C_Y)
                    break
            for i in range(N):
                if data[i][2] != max(H - abs(data[i][0] - C_X) - abs(data[i][1] - C_Y), 0):
                    break
            else:
                print(C_X, C_Y, H)
                return

if __name__ == '__main__':
    main()