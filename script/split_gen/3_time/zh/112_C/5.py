def main():
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    for i in range(N):
        if data[i][2] > 0:
            C_X = data[i][0]
            C_Y = data[i][1]
            H = data[i][2]
    for C_X in range(101):
        for C_Y in range(101):
            for i in range(N):
                if data[i][2] > 0:
                    H = data[i][2] + abs(data[i][0] - C_X) + abs(data[i][1] - C_Y)
            for i in range(N):
                if data[i][2] == 0:
                    if H - abs(data[i][0] - C_X) - abs(data[i][1] - C_Y) > 0:
                        break
                    else:
                        if i == N - 1:
                            print(C_X, C_Y, H)
    return None
