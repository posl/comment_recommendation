def main():
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    for x in range(101):
        for y in range(101):
            H = -1
            for i in range(N):
                if data[i][2] > 0:
                    H = data[i][2] + abs(data[i][0] - x) + abs(data[i][1] - y)
                    break
            if H == -1:
                continue
            f = True
            for i in range(N):
                if data[i][2] != max(H - abs(data[i][0] - x) - abs(data[i][1] - y), 0):
                    f = False
                    break
            if f:
                print(x, y, H)
                exit()

if __name__ == '__main__':
    main()