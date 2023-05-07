def main():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    ans = [0] * w
    for i in range(w):
        for j in range(h):
            if grid[j][i] == '#':
                ans[i] += 1
    print(' '.join(map(str, ans)))
