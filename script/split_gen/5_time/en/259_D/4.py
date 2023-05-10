def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = [list(map(int, input().split())) for _ in range(N)]
    #print(N, sx, sy, tx, ty)
    #print(circles)
    for i in range(N):
        x, y, r = circles[i]
        if (x - sx) ** 2 + (y - sy) ** 2 < r ** 2 and (x - tx) ** 2 + (y - ty) ** 2 < r ** 2:
            print('No')
            return
    print('Yes')
