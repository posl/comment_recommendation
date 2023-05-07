def main():
    N = int(input())
    XYH = [list(map(int, input().split())) for _ in range(N)]
    XYH.sort(key=lambda x: x[2], reverse=True)
    for x in range(101):
        for y in range(101):
            h = XYH[0][2] + abs(XYH[0][0] - x) + abs(XYH[0][1] - y)
            for i in range(N):
                if XYH[i][2] != max(h - abs(XYH[i][0] - x) - abs(XYH[i][1] - y), 0):
                    break
            else:
                print(x, y, h)
                return
