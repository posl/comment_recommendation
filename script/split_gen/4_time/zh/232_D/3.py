def main():
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(input())
    ans = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '.':
                ans += 1
    print(ans)
