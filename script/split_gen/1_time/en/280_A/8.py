def main():
    h, w = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(input()))
    print(sum(row.count('#') for row in grid))
