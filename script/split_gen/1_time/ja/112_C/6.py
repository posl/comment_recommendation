def main():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x: x[2], reverse=True)
    for C_X in range(101):
        for C_Y in range(101):
            H = data[0][2] + abs(data[0][0] - C_X) + abs(data[0][1] - C_Y)
            for i in range(1, N):
                if H - abs(data[i][0] - C_X) - abs(data[i][1] - C_Y) != data[i][2]:
                    break
            else:
                print(C_X, C_Y, H)
                return
