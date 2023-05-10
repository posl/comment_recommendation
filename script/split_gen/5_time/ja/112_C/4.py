def main():
    N = int(input())
    xyh = [list(map(int, input().split())) for _ in range(N)]
    xyh.sort(key=lambda x:x[2], reverse=True)
    for cx in range(101):
        for cy in range(101):
            H = xyh[0][2] + abs(cx - xyh[0][0]) + abs(cy - xyh[0][1])
            for i in range(1, N):
                if xyh[i][2] != max(H - abs(cx - xyh[i][0]) - abs(cy - xyh[i][1]), 0):
                    break
            else:
                print(cx, cy, H)
                return
