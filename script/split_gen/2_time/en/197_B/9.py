def main():
    # Take the input
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    # Start from (X, Y) and go in all 4 directions
    # until you hit a wall or an obstacle
    count = 1
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        x, y = X-1, Y-1
        while True:
            x += dx
            y += dy
            if x < 0 or x >= H or y < 0 or y >= W or S[x][y] == '#':
                break
            count += 1
    # Print the answer
    print(count)
