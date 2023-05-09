def main():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    #print(data)
    for cx in range(101):
        for cy in range(101):
            h = 0
            for x, y, h0 in data:
                if h0 > 0:
                    h = h0 + abs(x - cx) + abs(y - cy)
                    break
            if h == 0:
                continue
            for x, y, h0 in data:
                if h0 != max(h - abs(x - cx) - abs(y - cy), 0):
                    break
            else:
                print(cx, cy, h)
                return
main()

if __name__ == '__main__':
    main()