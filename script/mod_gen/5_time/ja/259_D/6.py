def main():
    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    circles = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    if ((sx, sy), (tx, ty)) in [(c1, c2) for c1 in circles for c2 in circles]:
        print('Yes')
        return
    def is_connected((x1, y1), (x2, y2), r):
        d = ((x1-x2)**2+(y1-y2)**2)**0.5
        if d <= r:
            return True
        return False
    def dfs(i, visited):
        if i == tx and j == ty:
            return True
        for j in range(n):
            if j in visited:
                continue
            if is_connected((i, j), (tx, ty), circles[j][2]):
                return dfs(j, visited + [j])
        return False
    for i in range(n):
        if is_connected((sx, sy), (circles[i][0], circles[i][1]), circles[i][2]):
            if dfs(i, [i]):
                print('Yes')
                return
    print('No')

if __name__ == '__main__':
    main()