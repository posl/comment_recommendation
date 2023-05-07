def main():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    for x in range(101):
        for y in range(101):
            H = -1
            for i in range(N):
                if data[i][2] > 0:
                    H = data[i][2] + abs(x - data[i][0]) + abs(y - data[i][1])
                    break
            if H == -1:
                continue
            flag = True
            for i in range(N):
                if max(H - abs(x - data[i][0]) - abs(y - data[i][1]), 0) != data[i][2]:
                    flag = False
                    break
            if flag:
                print(x, y, H)
                return

if __name__ == '__main__':
    main()