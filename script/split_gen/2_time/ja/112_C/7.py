def main():
    n = int(input())
    data = [list(map(int, input().split())) for i in range(n)]
    for cx in range(101):
        for cy in range(101):
            for h in range(101):
                if all(h == max(h - abs(cx - x) - abs(cy - y), 0) for x, y, h in data):
                    print(cx, cy, h)
                    return
