def main():
    n = int(input())
    xyh = [list(map(int, input().split())) for _ in range(n)]
    xyh.sort(key=lambda x: x[2], reverse=True)
    for cx in range(101):
        for cy in range(101):
            h = xyh[0][2] + abs(xyh[0][0]-cx) + abs(xyh[0][1]-cy)
            for i in range(1, n):
                if xyh[i][2] != max(h - abs(xyh[i][0]-cx) - abs(xyh[i][1]-cy), 0):
                    break
            else:
                print(cx, cy, h)
                return
main()

if __name__ == '__main__':
    main()