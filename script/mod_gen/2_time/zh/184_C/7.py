def bfs(r1, c1, r2, c2):
    if r1 == r2 and c1 == c2:
        return 0
    visited = set()
    visited.add((r1, c1))
    queue = [(r1, c1)]
    step = 0
    while queue:
        step += 1
        for _ in range(len(queue)):
            r, c = queue.pop(0)
            for i in range(-3, 4):
                for j in range(-3, 4):
                    if (r + i, c + j) not in visited:
                        if r + i == r2 and c + j == c2:
                            return step
                        if r + i + c + j == r2 + c2 or r + i - c - j == r2 - c2 or abs(r + i - r2) + abs(c + j - c2) <= 3:
                            visited.add((r + i, c + j))
                            queue.append((r + i, c + j))
    return -1

if __name__ == '__main__':
    bfs()