def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = [tuple(map(int, input().split())) for _ in range(N)]
    def dist(x1, y1, x2, y2):
        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    def reachable(x1, y1, x2, y2):
        for cx, cy, r in circles:
            if dist(x1, y1, cx, cy) < r and dist(x2, y2, cx, cy) < r:
                return True
        return False
    if reachable(sx, sy, tx, ty):
        print('Yes')
    else:
        print('No')
