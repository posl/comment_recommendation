def main():
    N = int(input())
    XYH = [list(map(int, input().split())) for _ in range(N)]
    for cx in range(101):
        for cy in range(101):
            for i in range(N):
                if XYH[i][2] != max(XYH[i][2] + abs(XYH[i][0] - cx) + abs(XYH[i][1] - cy), 0):
                    break
            else:
                print(cx, cy, XYH[i][2] + abs(XYH[i][0] - cx) + abs(XYH[i][1] - cy))
                exit()
    return
