def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ret = []
    for y in range(h):
        for x in range(w):
            if a[y][x] % 2 == 1:
                if x < w-1:
                    a[y][x+1] += 1
                    ret.append((y+1, x+1, y+1, x+2))
                elif y < h-1:
                    a[y+1][x] += 1
                    ret.append((y+1, x+1, y+2, x+1))
    print(len(ret))
    for y1, x1, y2, x2 in ret:
        print(y1, x1, y2, x2)
