def main():
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    for cx in range(101):
        for cy in range(101):
            h = 0
            for x, y, h0 in data:
                if h0 == 0:
                    continue
                h = h0 + abs(cx - x) + abs(cy - y)
                break
            for x, y, h0 in data:
                if h0 != max(h - abs(cx - x) - abs(cy - y), 0):
                    break
            else:
                print(cx, cy, h)
                return
